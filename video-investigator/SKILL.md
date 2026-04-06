---
name: video-investigator
description: Analyze and investigate videos by extracting frames using ffmpeg. Uses a binary search approach — extract a low-fps overview first, then zoom into specific times of interest at higher framerates. Use when asked to inspect, debug, or find issues in video files.
allowed-tools: Bash(ffmpeg*), Bash(ffprobe*), Bash(bash */video-investigator/scripts/*), Bash(rm -rf */video-investigator/tmp/*), Bash(command -v ffmpeg*), Bash(command -v ffprobe*), Read
---

# video-investigator

## Description
Analyze and investigate videos efficiently by extracting frames to a temporary directory. This skill uses a "zoom in" (binary search) approach: extract a 1–5fps overview first based on the video's total duration, then zoom into specific times of interest to extract more frames. This prevents context bloat and speeds up the investigation.

## Preconditions
`ffmpeg` and `ffprobe` must be available on your path before starting.
```bash
# Check if installed
command -v ffmpeg && command -v ffprobe
```

If either command is missing, pause the investigation and help the user get set up before continuing. Tell them plainly that this skill depends on `ffmpeg`/`ffprobe`, share the install command for their platform, and ask them to rerun the check after installation.

Use these setup instructions:
- **macOS (Homebrew):** `brew install ffmpeg`
- **Linux (Debian/Ubuntu):** `sudo apt update && sudo apt install -y ffmpeg`
- **Windows (winget):** `winget install ffmpeg`

After installation, have the user verify it worked:
```bash
ffmpeg -version && ffprobe -version
```

If verification still fails, explain that they may need to open a new terminal so their `PATH` refreshes, then run the verification command again.

## Instructions

**Important: Communication**
Throughout the investigation process, frequently communicate your current step to the user in plain text. Do not just run bash commands silently. Tell the user what you are doing, for example:
- "Starting initial investigation..."
- "Found issue at around 00:15."
- "Detailed 'zooming' on a certain range (00:14-00:16) at 10 fps..."
- "Pinpointed the exact frame, extracting for final review."

1. **Check Video Duration:**
   Find out how long the video is to decide your overview framerate. Before starting, tell the user you are doing the "initial investigation".
   ```bash
   bash ${__DIR__}/scripts/probe_video.sh <video_path>
   ```

2. **Extract Overview (1-5 fps):**
   Extract a low framerate overview to the skill's pre-approved temp directory.
   ```bash
   bash ${__DIR__}/scripts/extract_frames.sh <video_path> 0 "end" <fps> "${__DIR__}/tmp/overview"
   ```
   *Note: Use 1fps for videos > 1 min, or up to 5fps for very short videos.*

3. **Review and "Zoom In" (Binary Search Approach):**
   Examine the overview frames using the `read` tool. When you spot what you're looking for, tell the user you "found issue" and mention the timestamp.
   Then extract frames *only* for that specific window at a higher framerate (e.g., 30fps), or use a smaller step. Tell the user you are doing a "detailed 'zooming' on a certain range".
   ```bash
   bash ${__DIR__}/scripts/extract_frames.sh <video_path> <start_time> <end_time> <high_fps> "${__DIR__}/tmp/zoom"
   ```
   *Repeat this zoom-in process until you find the exact detail required.*

4. **Extract a Single Frame (If needed):**
   If you pinpoint an exact timestamp you want to inspect:
   ```bash
   bash ${__DIR__}/scripts/extract_single_frame.sh <video_path> <timestamp> "${__DIR__}/tmp/frame.jpg"
   ```

5. **Clean Up:**
   When you're finished, ALWAYS clean up the temporary directory to save disk space and keep things tidy.
   ```bash
   rm -rf "${__DIR__}/tmp/"*
   ```

## Directory Access
To prevent permission errors, all frame extraction should be output to this skill's `tmp` directory (`${__DIR__}/tmp/`). Because it resides within the workspace, `pi` is pre-approved to read and write to it. Do not attempt to write temp files to the system `/tmp` or other locations outside the workspace unless explicitly permitted by the user.

## Scripts Included
- `probe_video.sh <path>`: Outputs video duration in seconds.
- `extract_frames.sh <path> <start_time> <end_time|end> <fps> <output_dir>`: Extracts frames using `ffmpeg` correctly.
- `extract_single_frame.sh <path> <timestamp> <output_file>`: Extracts just one frame at a specific timestamp.
