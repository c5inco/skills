---
id: 21-tabs-at-12
category: howto
difficulty: medium
---

## Prompt

> My app has 12 tabs for different views. How should I handle them?

## Expected skill behavior

1. Flags the count: **auto-hide / collapse into a dropdown at 8+ tabs** per the IntelliJ Tabs guideline. 12 is well past that threshold.
2. **Never disable tabs** — if some are unavailable, explain the unavailability inside the tab content, not by disabling the tab itself.
3. Keeps tab labels short: **max 3 words**.
4. Positions tabs above their content, with alignment to the container borders.
5. Uses Jewel `Tabs` / `TabStrip`.

## Pass criteria

- [ ] Flags that 12 is too many to display flat; recommends auto-hiding overflow (typically into a dropdown or "more" affordance) at 8+.
- [ ] States that tabs should **never be disabled** — unavailability explained in the tab content instead.
- [ ] Mentions the short-label convention (≤3 words) or similar tab-label guidance.
- [ ] Uses Jewel `Tabs` / `TabStrip` (or points at them); does not propose Material tabs or a hand-rolled solution.

## Notes

The "auto-hide at 8+" and "never disable" rules are both specific to the IntelliJ Tabs guideline. The prompt is deliberately under-specified to see whether the skill volunteers these rules unprompted.

Source: [Tabs guideline](https://plugins.jetbrains.com/docs/intellij/tabs.html).
