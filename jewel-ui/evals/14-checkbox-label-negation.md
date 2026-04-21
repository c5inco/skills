---
id: 14-checkbox-label-negation
category: howto
difficulty: medium
---

## Prompt

> I need a checkbox that lets users disable email notifications. How should I label it?

## Expected skill behavior

1. Notices the word "disable" in the prompt plants a negation seed — the naive answer is a label like "Disable email notifications", which violates the IntelliJ no-negation rule.
2. Routes to COMPONENT-SELECTION.md "Writing Component Labels" section.
3. Recommends positive phrasing where the off state (unchecked) naturally means "notifications off" — e.g. `"Send email notifications"`, `"Enable email notifications"`, or just `"Email notifications"`.
4. Uses `Checkbox` / `CheckboxRow`.
5. May also mention the guideline escape hatch: if the off-state meaning is unclear from the label, switch to two `RadioButton`s with explicit labels for both states.

## Pass criteria

- [ ] The label shown in the answer uses **positive phrasing** (e.g. "Send email notifications", "Email notifications on", "Enable email notifications"). It is **not** "Disable email notifications" or any equivalent negation.
- [ ] Uses `CheckboxRow` or `Checkbox` — not a `Button`, `Toggle`, or hand-composed control.
- [ ] Explicitly addresses the avoid-negation rule (cites the convention, explains why, or mentions the `"Do not show again"` exception).
- [ ] Correctly orients checked/unchecked (checked = notifications are on) so the positive label and the state map consistently.

## Notes

This eval is designed to expose the skill's label-writing depth. The prompt itself contains "disable", which is the naive framing; the correct answer inverts the phrasing rather than mirroring the prompt's word choice. Baseline and current should now score similarly since the rolled baseline also contains COMPONENT-SELECTION.md.

Source: [Checkbox guideline](https://plugins.jetbrains.com/docs/intellij/checkbox.html).
