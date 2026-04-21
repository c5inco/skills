---
id: 25-validation-error-presentation
category: howto
difficulty: medium
---

## Prompt

> A form field failed validation — the user entered an invalid email. How should I present the error?

## Expected skill behavior

1. Uses an inline error below the field — not a `Dialog`, not a `Tooltip`, not a toast / `Notification`.
2. Applies a red outline to the field via `JewelTheme.globalColors.outlines.error` (or `focusedError` when the field has focus).
3. Pairs the outline with short error text styled via `JewelTheme.globalColors.text.error` using `JewelTheme.typography.small` or `InfoText`.
4. The message is short, imperative, and actionable ("Enter a valid email address"), not generic ("Invalid input" or "Error").
5. Does not reach for `InlineBanner` for a single-field validation error — banners are for component-level state, not field-level.

## Pass criteria

- [ ] Places the error inline, immediately below (or adjacent to) the offending field — not in a dialog, tooltip, or notification.
- [ ] Applies an error outline to the field via `JewelTheme.globalColors.outlines.error` / `focusedError` (or explicitly mentions those semantic tokens).
- [ ] Uses an error-colored text for the message via `JewelTheme.globalColors.text.error` (semantic, not hardcoded hex).
- [ ] Recommends short, specific, actionable error text (not a generic "Error" or "Invalid").

## Notes

This eval closes a run-8 follow-up: validation errors were flagged as uncovered. The rule is a composite of the Input Field, Validation Errors, and Platform Theme Colors principles — a good stress-test of semantic-color usage.

Sources: [Input Field](https://plugins.jetbrains.com/docs/intellij/input-field.html), [Validation Errors](https://plugins.jetbrains.com/docs/intellij/validation-errors.html).
