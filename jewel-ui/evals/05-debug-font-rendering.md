---
id: 05-debug-font-rendering
category: debug
difficulty: medium
---

## Prompt

> My standalone Jewel app's fonts look wrong — what am I missing?

## Expected skill behavior

1. Identifies JetBrains Runtime (JBR) as the most common root cause of font/rendering issues in standalone Jewel apps, per STANDALONE-VS-BRIDGE.md and the Implementation Checklist.
2. Provides a concrete remediation step (configure `javaHome` for Compose Desktop, or verify the app is launching on JBR).
3. Does not start with font-API-level tweaks as the first fix.

## Pass criteria

- [ ] Response mentions JetBrains Runtime (JBR) explicitly.
- [ ] Identifies JBR absence/mismatch as the likely root cause rather than leading with font styling guidance.
- [ ] Provides actionable fix (e.g. point `javaHome` at a JBR install, or verify runtime).
- [ ] Does not suggest overriding `JewelTheme.createDefaultTextStyle()` as the first step.
