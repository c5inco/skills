---
id: 17-tooltip-on-icon-button
category: howto
difficulty: medium
---

## Prompt

> I have an `IconButton` with just an icon. Do I need anything else?

## Expected skill behavior

1. Answers: **yes** — every icon-only / unlabeled interactive control must be wrapped in a `Tooltip` per the IntelliJ Tooltip guideline.
2. The Tooltip content should include both the action name and the keyboard shortcut (if one exists).
3. Uses Jewel's `Tooltip` / `TooltipArea` composable.
4. Does not wave off the requirement with "only if the icon isn't obvious" or similar — the rule applies uniformly.

## Pass criteria

- [ ] Explicitly answers that yes, additional structure (a Tooltip) is required — not optional, not conditional.
- [ ] Recommends wrapping the `IconButton` in a Jewel `Tooltip` / `TooltipArea`.
- [ ] Mentions including the action name and the keyboard shortcut (or explicitly notes both belong in the tooltip content).
- [ ] Also correct: meaningful `contentDescription` on the `Icon` itself (accessibility), distinct from the visible tooltip.

## Notes

This eval tests whether the skill enforces the "every icon MUST have a tooltip" rule as a directive, not as a soft suggestion. The prompt invites a "that's enough" answer; the right answer is pushback.

Source: [Tooltip guideline](https://plugins.jetbrains.com/docs/intellij/tooltip.html).
