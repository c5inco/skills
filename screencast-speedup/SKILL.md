---
name: screencast-speedup
description: >-
  Process developer demo screencasts showing AI coding assistants and interactive app testing.
  Speeds up LLM generation and builds (8x), briskly speeds up prompt feedback typing (2x),
  preserves real-time app interaction and initial context (1x), and dynamically applies
  speed-ramping cushions to smooth scene transitions.
---

# Screencast Speedup & Transition Smoothing Runbook

Use this skill when processing raw screen recordings that feature developers steering AI coding assistants (like Gemini, Antigravity, Claude, Copilot) and testing the resulting mobile apps, web applications, or desktop tools.

---

## 1. Pacing & Speed Hierarchy

Follow this tier system when editing screencasts:

| Segment Type | Target Speed | Rationale |
| :--- | :--- | :--- |
| **Initial Prompt & Goal** | **1.0x** | Establishes project context and lets the viewer read the objective (first 5–10s). |
| **Active App & UI Testing** | **1.0x** | Preserves all real-time touch gestures, sliders, scrolling, and responsiveness. |
| **Follow-up Prompt Typing** | **2.0x** | Makes feedback typing and steering feel brisk without skipping content. |
| **LLM Generation & Build** | **8.0x** | Fast-forwards long token generation, file navigation, and Gradle/compiler compilation. |
| **Transition Cushions** | **2.0x** | Deceleration buffer (4–6s) before switching to the app; acceleration buffer (3–5s) after sending prompts. |
| **Summary & Wrap-up** | **1.0x** | Concludes the video cleanly. |

For detailed guidelines, see [pacing-guidelines.md](./references/pacing-guidelines.md).

---

## 2. Step-by-Step Workflow

### Step 1: Inspect Video & Extract Metadata
Run `ffprobe` to find the duration and resolution:
```bash
ffprobe -v error -show_entries format=duration -show_streams -of json <input_video.mp4>
```

### Step 2: Identify Timestamps & Classify Segments
Extract sample frames around major milestones (prompt sends, builds, tab switches) using [sample_frames.py](./scripts/sample_frames.py):
```bash
python3 .agents/skills/screencast-speedup/scripts/sample_frames.py \
  -i <input_video.mp4> \
  --interval 15.0 \
  -o /tmp/screencast_samples
```

Create a timeline JSON file (e.g. `timeline.json`):
```json
[
  {"start": 0.0, "end": 7.0, "speed": 1.0, "description": "Initial Prompt Review & Send"},
  {"start": 7.0, "end": 213.8, "speed": 8.0, "description": "LLM Generation & Gradle Build 1"},
  {"start": 213.8, "end": 232.2, "speed": 1.0, "description": "Phone App Testing 1"},
  {"start": 232.2, "end": 262.0, "speed": 2.0, "description": "Prompt 2 Typing & Steering"},
  {"start": 262.0, "end": 354.2, "speed": 8.0, "description": "LLM Generation & Build 2"},
  {"start": 354.2, "end": 375.2, "speed": 1.0, "description": "Phone App Testing 2"},
  {"start": 375.2, "end": 391.0, "speed": 2.0, "description": "Prompt 3 Typing & Steering"},
  {"start": 391.0, "end": 507.2, "speed": 8.0, "description": "LLM Generation & Build 3"},
  {"start": 507.2, "end": 572.0, "speed": 1.0, "description": "Phone App Testing 3"},
  {"start": 572.0, "end": 587.2, "speed": 1.0, "description": "Wrap-up & Summary"}
]
```

### Step 3: Render with Automatic Speed Ramping
Execute [process_screencast.py](./scripts/process_screencast.py). It automatically inserts deceleration cushions before app interactions and acceleration cushions after prompt submissions:
```bash
python3 .agents/skills/screencast-speedup/scripts/process_screencast.py \
  --input <input_video.mp4> \
  --timeline timeline.json \
  --output <output_video.mp4> \
  --ramp-sec 4.0 \
  --ramp-speed 2.0 \
  --crf 18 \
  --preset fast
```

### Step 4: Verify Output
Verify the output duration and visual quality:
```bash
ffprobe -v error -show_entries format=duration,size -of json <output_video.mp4>
```

---

## 3. Reference Documentation

- [Pacing & Speed Guidelines](./references/pacing-guidelines.md)
- [FFmpeg Filtergraph Technical Reference](./references/ffmpeg-filtergraphs.md)
