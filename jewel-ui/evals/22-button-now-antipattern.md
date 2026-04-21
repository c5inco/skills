---
id: 22-button-now-antipattern
category: howto
difficulty: easy
---

## Prompt

> Label a button that applies a settings change — should it say "Apply Now" or "Apply"?

## Expected skill behavior

1. Picks "Apply" and flags "Now" as a button-label anti-pattern per the IntelliJ Button guideline.
2. Cites the rule: avoid "Now"; title case; imperative verb; max 5 words.
3. Uses Jewel `DefaultButton` (primary action).
4. Does not propose alternatives like "Save Changes Now" or "Apply Changes Now".

## Pass criteria

- [ ] Picks "Apply" (without "Now").
- [ ] Explicitly flags "Now" as unnecessary or against convention — cites a rule or explains why ("Now" doesn't add information; the button is implicitly immediate).
- [ ] Uses `DefaultButton` (primary action).
- [ ] Uses title case for the button label (distinct from sentence case for checkboxes/radios). "Apply", not "apply".

## Notes

This is a narrow label-rule eval; scoreable in one glance. The "Now" rule is specific to the IntelliJ Button guideline and not broadly-known Compose/UX knowledge.

Source: [Button guideline](https://plugins.jetbrains.com/docs/intellij/button.html).
