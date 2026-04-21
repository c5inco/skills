---
id: 07-disable-button
category: howto
difficulty: easy
---

## Prompt

> How do I disable a Jewel Button?

## Expected skill behavior

1. Directly answers using the standard Compose `enabled: Boolean` parameter pattern.
2. Does not gate the answer on Jewel version, platform version, or require inspecting build files first — this prompt needs none of that.

## Pass criteria

- [ ] Answer shows the `enabled = false` parameter on `DefaultButton` (or an equivalent Jewel button).
- [ ] Uses a Jewel button (`DefaultButton` / `OutlinedButton`), not `androidx.compose.material.*`.
- [ ] Does NOT ask "what Jewel version?" or "can you share your build files?" before answering — this is a negative test for Version Discipline over-asking.
- [ ] Does not hand-roll disabled appearance (e.g. hardcoded gray color); relies on the component's built-in disabled style.
