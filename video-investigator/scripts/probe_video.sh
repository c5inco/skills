#!/usr/bin/env bash
# probe_video.sh <video_path>
# Returns duration of video in seconds

VIDEO_PATH="$1"

if [ -z "$VIDEO_PATH" ]; then
  echo "Usage: $0 <video_path>"
  exit 1
fi

ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "$VIDEO_PATH"
