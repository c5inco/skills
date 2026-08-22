#!/usr/bin/env python3
"""
sample_frames.py

Helper script to sample and inspect video frames at interval timestamps
to classify scenes and pinpoint transition points.
"""

import argparse
import os
import subprocess
import sys


def main():
    parser = argparse.ArgumentParser(description="Sample video frames at given timestamps or regular intervals.")
    parser.add_argument("--input", "-i", required=True, help="Input video file path")
    parser.add_argument("--output-dir", "-o", default="/tmp/screencast_samples", help="Output directory for sample images")
    parser.add_argument("--timestamps", "-t", nargs="+", type=float, help="Explicit list of timestamps (seconds) to extract")
    parser.add_argument("--interval", type=float, help="Extract 1 frame every N seconds")
    parser.add_argument("--scale", default="360", help="Horizontal thumbnail scale width (default: 360)")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.input):
        print(f"Error: Video file not found at {args.input}", file=sys.stderr)
        sys.exit(1)
        
    os.makedirs(args.output_dir, exist_ok=True)
    
    timestamps = []
    if args.timestamps:
        timestamps = args.timestamps
    elif args.interval:
        # Get duration
        cmd = ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", args.input]
        res = subprocess.run(cmd, capture_output=True, text=True)
        dur = float(res.stdout.strip())
        t = 0.0
        while t < dur:
            timestamps.append(t)
            t += args.interval
    else:
        print("Please provide either --timestamps or --interval", file=sys.stderr)
        sys.exit(1)
        
    print(f"Extracting {len(timestamps)} frame samples into {args.output_dir} ...")
    for t in timestamps:
        out_img = os.path.join(args.output_dir, f"frame_{t:07.2f}s.jpg")
        cmd = [
            "ffmpeg", "-y", "-ss", str(t), "-i", args.input,
            "-frames:v", "1", "-vf", f"scale={args.scale}:-1",
            out_img
        ]
        subprocess.run(cmd, capture_output=True)
        print(f"  Captured: {out_img}")
        
    print("Done!")


if __name__ == "__main__":
    main()
