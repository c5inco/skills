---
id: 11-subscription-tier-form
category: howto
difficulty: medium
---

## Prompt

> I need a form where the user picks a subscription tier: Free, Pro, or Enterprise. Show me how to build it with Jewel.

## Expected skill behavior

1. Classifies the interaction as mutually exclusive pick from a small set of options.
2. Routes to COMPONENT-SELECTION.md "Mutually Exclusive Selection" rule.
3. Picks `RadioButton` / `RadioButtonRow` — not three `DefaultButton`s.
4. Groups under a `GroupHeader` whose label ends with `:`.
5. State is a single value (enum, sealed class, or index), not three booleans.
6. Includes a separate, visually distinct submit/confirm button.

## Pass criteria

- [ ] Uses `RadioButton`, `RadioButtonRow`, or `RadioButtonChip` for the three-way selection.
- [ ] Does **not** use three separate `DefaultButton` / `OutlinedButton` / `Button` composables as the selection mechanism.
- [ ] Selection state is a single value (e.g. `mutableStateOf(Tier.Free)` or a single `selectedIndex`), not three independent booleans.
- [ ] Group is introduced with a `GroupHeader` whose label ends with `:` (e.g. "Subscription tier:").
- [ ] Submit/confirm action is a separate button, distinct from the selection controls.
- [ ] Option labels do not use negation.

## Notes

This eval tests the "compositional taste" gap — picking the right component for the interaction, not the first one that works. Source of truth: [Radio Button guideline](https://plugins.jetbrains.com/docs/intellij/radio-button.html).
