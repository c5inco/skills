---
id: 13-settings-toggles
category: howto
difficulty: medium
---

## Prompt

> I have a settings page with about 10 preference toggles — things like "Show line numbers", "Word wrap", "Auto-save on focus lost". How should I lay them out?

## Expected skill behavior

1. Classifies as multi-select of independent booleans.
2. Routes to COMPONENT-SELECTION.md "Multi-Select and Toggles" rule.
3. Uses `CheckboxRow` per toggle, laid out in a vertical `Column` with `Arrangement.spacedBy`.
4. Uses `GroupHeader` for section divisions — not `Divider` between every toggle and not wrapping each in its own `Card`.
5. Labels are short, imperative, and avoid negation.

## Pass criteria

- [ ] Uses `CheckboxRow` (or `Checkbox`) for each toggle — not a `Button` or `SegmentedControl` or one-off custom composable.
- [ ] Arranges toggles in a vertical `Column` with a consistent spacing primitive (e.g. `Arrangement.spacedBy(...)`), not ad-hoc per-item padding.
- [ ] Uses `GroupHeader` for section titles when grouping is shown — not `Divider` on every boundary, and not one `Card` per row.
- [ ] Toggle labels are short, imperative, and avoid negation ("Show line numbers", not "Do not hide line numbers").
- [ ] Does not hardcode colors for active/inactive state; relies on the component's built-in styling.

## Notes

Source: [Checkbox guideline](https://plugins.jetbrains.com/docs/intellij/checkbox.html) and the group-of-controls [Layout](https://plugins.jetbrains.com/docs/intellij/layout.html) principle.
