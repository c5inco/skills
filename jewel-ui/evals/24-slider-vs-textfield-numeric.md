---
id: 24-slider-vs-textfield-numeric
category: howto
difficulty: medium
---

## Prompt

> I need the user to pick a value between 0 and 100 for volume.

## Expected skill behavior

1. Picks `Slider` (the Jewel `Slider` component) — volume is a continuous bounded value with direct-manipulation intent.
2. May mention the trade-off: use `TextField` (with numeric validation) if the user needs precise entry; use `Slider` when direct-manipulation feels right.
3. Uses Jewel's `Slider` composable; does not hand-roll a slider from primitives.
4. Correctly sets the value range (`0f..100f` or equivalent).

## Pass criteria

- [ ] Picks `Slider` as the primary recommendation (not `TextField` alone, not a combo box, not a segmented control).
- [ ] Correctly sets the range to match 0–100 (e.g. `valueRange = 0f..100f`).
- [ ] Uses Jewel's `Slider` — not a hand-composed slider or Material's `Slider`.
- [ ] Optionally mentions pairing with a numeric display / `TextField` if the user also needs precise-entry — this is a quality-of-reasoning bonus but not required.

## Notes

Tests the "Slider for continuous numeric with direct-manipulation intent" pick. The IntelliJ guidelines don't have a dedicated Slider page (it's a "(no page)" entry in the TOC), so this rule comes from the Jewel catalog + general UX convention.

This eval fills a long-standing gap: `Slider` appears in COMPONENTS-CATALOG.md but has no selection rule anywhere in the skill.
