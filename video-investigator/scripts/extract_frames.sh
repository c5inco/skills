#!/usr/bin/env bash
# extract_frames.sh <video_path> <start_time> <end_time> <fps> <output_dir>
# Use "end" or "" for end_time to process until the end of the video.

VIDEO_PATH="$1"
START_TIME="$2"
END_TIME="$3"
FPS="$4"
OUTPUT_DIR="$5"

if [ -z "$OUTPUT_DIR" ]; then
  echo "Usage: $0 <video_path> <start_time> <end_time> <fps> <output_dir>"
  exit 1
fi

mkdir -p "$OUTPUT_DIR"

if [ -z "$END_TIME" ] || [ "$END_TIME" = "end" ]; then
  ffmpeg -y -v error -ss "$START_TIME" -i "$VIDEO_PATH" -vf "fps=$FPS" -q:v 2 "$OUTPUT_DIR/frame_%04d.jpg"
else
  DURATION=$(awk -v e="$END_TIME" -v s="$START_TIME" 'BEGIN {print e - s}')
  ffmpeg -y -v error -ss "$START_TIME" -t "$DURATION" -i "$VIDEO_PATH" -vf "fps=$FPS" -q:v 2 "$OUTPUT_DIR/frame_%04d.jpg"
fi

echo "Extracted frames to $OUTPUT_DIR:"
ls -lh "$OUTPUT_DIR" | head -n 10
echo "... (showing top 10 files)"
