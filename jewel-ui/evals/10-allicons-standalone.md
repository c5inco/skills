---
id: 10-allicons-standalone
category: explain
difficulty: easy
---

## Prompt

> Can I use `AllIconsKeys` in a standalone Compose Desktop app?

## Expected skill behavior

1. Answers: yes, with conditions — routes to ICONS.md "Use IntelliJ platform icons" section.
2. Names the required dependency: `com.jetbrains.intellij.platform:icons:[ijpVersion]`.
3. Mentions adding the matching IntelliJ repository.
4. Does not imply `AllIconsKeys` works out-of-the-box in standalone the way it does in plugin context.

## Pass criteria

- [ ] Answer is clearly "yes, with conditions" — not "no" or "only in plugins".
- [ ] Mentions the `com.jetbrains.intellij.platform:icons` artifact (or equivalent Maven coordinate) by name.
- [ ] Mentions adding an IntelliJ repository to pull the artifact from.
- [ ] Does not claim `AllIconsKeys` is automatically available in standalone.
