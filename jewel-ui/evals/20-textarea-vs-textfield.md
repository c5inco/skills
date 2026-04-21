---
id: 20-textarea-vs-textfield
category: howto
difficulty: easy
---

## Prompt

> I want a commit message input field.

## Expected skill behavior

1. Picks `TextArea` — not `TextField` — because commit messages are multi-line, contain valid newlines, and can grow long.
2. Mentions sizing conventions: minimum ~3 lines high, width ~270–600px (80 columns).
3. Uses Jewel's `TextArea` composable.
4. May cite the rule: when content is unconstrained/multi-line with valid newlines, use `TextArea`; when it's a few words on one line, use `TextField`.

## Pass criteria

- [ ] Picks `TextArea` (not `TextField`) as the primary recommendation.
- [ ] Mentions multi-line / newline handling as the reason — not just "text input".
- [ ] Mentions minimum height (~3 lines / ~55px) or sensible width (~270–600px / ~80 columns), or flags sizing as important.
- [ ] Uses the Jewel `TextArea` composable; does not suggest Material `OutlinedTextField` or similar.

## Notes

Simple component-selection eval. The rule ("multi-line content → TextArea; single-line → TextField") is in the IntelliJ guideline but not yet encoded explicitly in the skill — this eval tests whether models reach for TextArea by default or default to TextField.

Source: [Text Area guideline](https://plugins.jetbrains.com/docs/intellij/text-area.html).
