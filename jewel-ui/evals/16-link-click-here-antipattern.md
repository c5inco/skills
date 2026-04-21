---
id: 16-link-click-here-antipattern
category: howto
difficulty: medium
---

## Prompt

> I have descriptive text explaining a setting, with a "click here" link to the docs.

## Expected skill behavior

1. Flags "click here" as a link-text anti-pattern per the IntelliJ Link guideline.
2. Rewrites the link text to be descriptive — the link itself should carry meaning.
3. Adds an external-link arrow when the destination is off-site (docs are external to the app).
4. Uses Jewel `Link`.
5. May mention the avoid list: "click here", "learn more", "navigate".

## Pass criteria

- [ ] Explicitly flags "click here" as wrong and gives a descriptive alternative (e.g. "Read the documentation", "View the migration guide").
- [ ] Recommends adding an arrow icon (external-link indicator) because docs are an external destination.
- [ ] Uses Jewel's `Link` component.
- [ ] Cites the rule (avoid "click here" / "learn more" / "navigate" / bare phrasings) or explains the reason (screen-reader traversal, scannability, link context clarity).

## Notes

Baseline may do well here — most models have general "don't write 'click here'" training. The value-add from the skill is the explicit external-link arrow rule.

Source: [Link guideline](https://plugins.jetbrains.com/docs/intellij/link.html).
