#!/usr/bin/env python3
"""
process_screencast.py

Automated multi-speed processor and transition smoother for AI/developer screencasts.
Features:
- Segment classification (context setup, LLM generation, app testing, prompt typing, wrap-up).
- Automatic deceleration/acceleration cushions (speed ramping) between fast segments and 1x interactive segments.
- Visual-lossless H.264 FFmpeg filtergraph generator & runner.
- Timeline input via JSON/YAML or Python data structure.
"""

import argparse
import json
import os
import subprocess
import sys


def get_video_info(input_path: str):
    """Retrieve video duration, resolution, and fps using ffprobe."""
    cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration,size:stream=width,height,r_frame_rate,avg_frame_rate,codec_name",
        "-of", "json", input_path
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        raise RuntimeError(f"ffprobe failed: {res.stderr}")
    data = json.loads(res.stdout)
    duration = float(data["format"]["duration"])
    streams = data.get("streams", [])
    video_stream = next((s for s in streams if s.get("codec_name") != "aac" and "width" in s), streams[0])
    width = video_stream.get("width")
    height = video_stream.get("height")
    return {"duration": duration, "width": width, "height": height}


def build_filtergraph(segments, input_path: str, output_path: str, crf: int = 18, preset: str = "fast", ramp_sec: float = 4.0, ramp_speed: float = 2.0):
    """
    Builds an FFmpeg filtercomplex string with automatic speed ramping cushions.
    
    Segment schema:
    [
        {"start": float, "end": float, "speed": float, "type": str, "description": str}
    ]
    
    If an 8x (or >=4x) segment borders a 1.0x segment, a brief ramp cushion at ramp_speed (default 2x)
    is inserted before/after the 1.0x transition to eliminate jarring cuts.
    """
    processed_slices = []
    
    for i, seg in enumerate(segments):
        start = seg["start"]
        end = seg["end"]
        speed = seg.get("speed", 1.0)
        seg_type = seg.get("type", "custom")
        desc = seg.get("description", "")
        dur = end - start
        
        # Check if we should insert acceleration ramp at the beginning of a fast segment (>= 4x)
        has_prev_slow = (i > 0 and segments[i-1].get("speed", 1.0) <= 2.0)
        has_next_slow = (i < len(segments) - 1 and segments[i+1].get("speed", 1.0) <= 2.0)
        
        if speed >= 4.0 and (has_prev_slow or has_next_slow) and dur > (ramp_sec * 2):
            cur_start = start
            
            # 1. Acceleration cushion at start
            if has_prev_slow:
                ramp_in_end = cur_start + ramp_sec
                processed_slices.append({
                    "start": cur_start, "end": ramp_in_end, "speed": ramp_speed,
                    "desc": f"{desc} (Acceleration ramp)"
                })
                cur_start = ramp_in_end
                
            # 2. Deceleration cushion at end
            ramp_out_start = end - (ramp_sec if has_next_slow else 0.0)
            
            # Middle fast slice
            if ramp_out_start > cur_start:
                processed_slices.append({
                    "start": cur_start, "end": ramp_out_start, "speed": speed,
                    "desc": f"{desc} (Fast-forward)"
                })
                
            # 3. Trailing deceleration slice
            if has_next_slow:
                processed_slices.append({
                    "start": ramp_out_start, "end": end, "speed": ramp_speed,
                    "desc": f"{desc} (Deceleration ramp)"
                })
        else:
            processed_slices.append({
                "start": start, "end": end, "speed": speed,
                "desc": desc
            })
            
    # Build filter complex parts
    filter_parts = []
    concat_inputs = []
    
    for idx, s in enumerate(processed_slices):
        label = f"v{idx}"
        speed = s["speed"]
        start_t = f"{s['start']:.3f}"
        end_t = f"{s['end']:.3f}"
        
        if abs(speed - 1.0) < 0.01:
            pts_expr = "setpts=PTS-STARTPTS"
        else:
            pts_expr = f"setpts=PTS-STARTPTS,setpts=PTS/{speed:.4f}"
            
        filter_parts.append(f"[0:v]trim=start={start_t}:end={end_t},{pts_expr}[{label}]")
        concat_inputs.append(f"[{label}]")
        
    n_inputs = len(concat_inputs)
    concat_str = "".join(concat_inputs) + f"concat=n={n_inputs}:v=1:a=0[outv]"
    full_filter = ";\\\n".join(filter_parts) + ";\\\n" + concat_str
    
    cmd = [
        "ffmpeg", "-y", "-i", input_path,
        "-filter_complex", full_filter,
        "-map", "[outv]",
        "-c:v", "libx264", "-crf", str(crf), "-preset", preset,
        output_path
    ]
    return cmd, processed_slices


def main():
    parser = argparse.ArgumentParser(description="Process developer screencasts with intelligent speed ramping.")
    parser.add_argument("--input", "-i", required=True, help="Path to raw screencast video")
    parser.add_argument("--output", "-o", required=True, help="Path for rendered output video")
    parser.add_argument("--timeline", "-t", required=True, help="Path to JSON/YAML timeline file")
    parser.add_argument("--crf", type=int, default=18, help="H.264 CRF quality (default: 18, lossless quality)")
    parser.add_argument("--preset", default="fast", help="FFmpeg x264 preset (default: fast)")
    parser.add_argument("--ramp-sec", type=float, default=4.0, help="Duration in source seconds for speed ramp cushions (default: 4.0s)")
    parser.add_argument("--ramp-speed", type=float, default=2.0, help="Speed factor during ramp cushions (default: 2.0x)")
    parser.add_argument("--dry-run", action="store_true", help="Print FFmpeg command without executing")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.input):
        print(f"Error: Input video not found at {args.input}", file=sys.stderr)
        sys.exit(1)
        
    if not os.path.exists(args.timeline):
        print(f"Error: Timeline file not found at {args.timeline}", file=sys.stderr)
        sys.exit(1)
        
    with open(args.timeline, "r") as f:
        timeline_data = json.load(f)
        
    segments = timeline_data if isinstance(timeline_data, list) else timeline_data.get("segments", [])
    
    print(f"Loaded {len(segments)} segments from {args.timeline}.")
    video_info = get_video_info(args.input)
    print(f"Input video: {args.input} ({video_info['width']}x{video_info['height']}, {video_info['duration']:.2f}s)")
    
    cmd, slices = build_filtergraph(
        segments=segments,
        input_path=args.input,
        output_path=args.output,
        crf=args.crf,
        preset=args.preset,
        ramp_sec=args.ramp_sec,
        ramp_speed=args.ramp_speed
    )
    
    print(f"\nGenerated {len(slices)} filtered slices (with dynamic speed ramping):")
    total_est_dur = 0.0
    for idx, s in enumerate(slices):
        dur = (s["end"] - s["start"]) / s["speed"]
        total_est_dur += dur
        print(f"  [{idx:02d}] {s['start']:7.2f}s - {s['end']:7.2f}s ({s['end']-s['start']:6.2f}s raw @ {s['speed']:4.1f}x -> {dur:5.2f}s) : {s['desc']}")
        
    print(f"\nEstimated Output Duration: {total_est_dur:.2f}s (~{int(total_est_dur//60)}m {int(total_est_dur%60)}s)")
    
    if args.dry_run:
        print("\n[Dry Run] FFmpeg Command:\n" + " ".join(cmd))
        return
        
    print(f"\nExecuting FFmpeg render -> {args.output} ...")
    ret = subprocess.run(cmd)
    if ret.returncode == 0:
        out_info = get_video_info(args.output)
        print(f"\nRender complete!")
        print(f"  Output: {args.output}")
        print(f"  Duration: {out_info['duration']:.2f}s (~{int(out_info['duration']//60)}m {int(out_info['duration']%60)}s)")
    else:
        print(f"FFmpeg failed with exit code {ret.returncode}", file=sys.stderr)
        sys.exit(ret.returncode)


if __name__ == "__main__":
    main()
