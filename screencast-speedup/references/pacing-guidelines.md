# Screencast Pacing & Speed Hierarchy Guidelines

When recording AI agent interactions and software demos, raw screen recordings are filled with long compilation steps, network waits, and verbose file exploration. Accelerating the entire video uniformly can ruin readability or make UI interactions impossible to follow.

This guide outlines the recommended speed hierarchy and transition principles.

---

## The 4-Tier Speed Hierarchy

### 1. **1.0x Real-Time (Interactive & Context Moments)**
- **Initial Setup & Context (First 5–10 seconds)**: Keep the starting prompt and goal at 1x so the viewer can read what is being built.
- **Active App & UI Testing**: Any screen where a mobile app, web UI, or CLI interface is being directly interacted with (touch gestures, scrolling, sliders, preset buttons, animations).
- **Wrap-up / Conclusion**: Final overview of the completed work or chat summary.

### 2. **2.0x Brisk Pacing (Steering & Follow-up Prompting)**
- **Follow-up Prompt Typing**: Typing feedback, correcting errors, steering the agent. 2x makes the typing feel snappy without skipping what was typed.
- **Speed Ramp Cushions**: Transition buffers between fast generation and real-time interaction.

### 3. **8.0x Fast-Forward (AI Generation & Compilation)**
- **Code Generation & Reasoning**: Long token generation, multi-file inspection, refactoring.
- **Compilation & Deployment**: `gradle assemble`, `npm build`, `docker build`, `adb install`, dev server spinups.
- *Note*: If 8x feels too fast for shorter 10-second tasks, use **4.0x**.

---

## Transition Smoothing & Speed Ramping (The Ease Cushion)

Hard cuts directly from `8.0x` into `1.0x` cause visual whip-crack (fast flashing text suddenly dead-stopping on a new screen). 

### How Speed Ramping Works
1. **Deceleration Buffer (`8.0x` $\rightarrow$ `2.0x` $\rightarrow$ `1.0x`)**:
   - In the final 4–6 seconds of source time before switching to the app (when the build succeeds and "Deployed successfully" appears), play that slice at **2.0x**.
   - The viewer sees the success notification at a readable pace and observes the tab switch before starting 1.0x testing.
2. **Acceleration Buffer (`1.0x / 2.0x` $\rightarrow$ `2.0x` $\rightarrow$ `8.0x`)**:
   - For 3–5 seconds after prompt submission, run at **2.0x** while the agent initializes before jumping to 8.0x.
