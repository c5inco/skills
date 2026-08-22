# FFmpeg Filtergraphs Reference for Multi-Speed Video

This document explains the technical syntax for building robust multi-speed filtergraphs in FFmpeg without audio/video desync or dropped PTS timestamps.

---

## 1. Speed Adjustment with `setpts`

In FFmpeg video filtergraphs, changing video speed requires manipulating the Presentation Time Stamp (`PTS`):

$$\text{Target PTS} = \frac{\text{PTS}}{\text{Speed}}$$

- For **8.0x speed**: `setpts=PTS/8.0` (or `setpts=0.125*PTS`)
- For **2.0x speed**: `setpts=PTS/2.0` (or `setpts=0.5*PTS`)
- For **1.0x speed**: `setpts=PTS-STARTPTS`

> [!IMPORTANT]
> Always reset timestamps with `PTS-STARTPTS` before scaling PTS. Otherwise, trimmed segments extracted from the middle of a file will retain their original offset, causing concat errors.

### Example Segment Filter:
```text
[0:v]trim=start=10.0:end=50.0,setpts=PTS-STARTPTS,setpts=PTS/8.0[v1]
```

---

## 2. Multi-Segment Slicing and `concat`

To combine multiple segments with different speeds:
```bash
ffmpeg -y -i input.mp4 -filter_complex "\
[0:v]trim=start=0:end=7.0,setpts=PTS-STARTPTS[v1];\
[0:v]trim=start=7.0:end=12.0,setpts=PTS-STARTPTS,setpts=PTS/2.0[v2a];\
[0:v]trim=start=12.0:end=200.0,setpts=PTS-STARTPTS,setpts=PTS/8.0[v2b];\
[0:v]trim=start=200.0:end=205.0,setpts=PTS-STARTPTS,setpts=PTS/2.0[v2c];\
[0:v]trim=start=205.0:end=230.0,setpts=PTS-STARTPTS[v3];\
[v1][v2a][v2b][v2c][v3]concat=n=5:v=1:a=0[outv]\
" -map "[outv]" -c:v libx264 -crf 18 -preset fast output.mp4
```

---

## 3. Recommended Encoding Flags

- **Codec**: `-c:v libx264` (universal compatibility across web, mobile, QuickTime)
- **CRF Quality**: `-crf 18` (visually indistinguishable from source)
- **Preset**: `-preset fast` (high encoding speed with small overhead)
- **Pixel Format**: `-pix_fmt yuv420p` (if re-encoding from non-standard colorspaces)
