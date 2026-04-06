#!/usr/bin/env bash
# extract_single_frame.sh <video_path> <timestamp> <output_file>

VIDEO_PATH="$1"
TIMESTAMP="$2"
OUTPUT_FILE="$3"

if [ -z "$OUTPUT_FILE" ]; then
  echo "Usage: $0 <video_path> <timestamp> <output_file>"
  exit 1
fi

OUTPUT_DIR=$(dirname "$OUTPUT_FILE")
mkdir -p "$OUTPUT_DIR"

ffmpeg -y -v error -ss "$TIMESTAMP" -i "$VIDEO_PATH" -frames:v 1 -q:v 2 "$OUTPUT_FILE"

echo "Extracted $OUTPUT_FILE"
