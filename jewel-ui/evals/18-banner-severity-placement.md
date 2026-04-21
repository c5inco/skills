---
id: 18-banner-severity-placement
category: howto
difficulty: medium
---

## Prompt

> I need to tell the user their workspace is out of sync — they should sync before making edits, but it's not blocking. How should I present this?

## Expected skill behavior

1. Routes to a Banner pattern (`DefaultBanner` or `InlineBanner`) — per the IntelliJ Banner guideline, banners cover contextual attention-needed states tied to a specific UI component, when attention is needed but not immediate.
2. Picks **Warning** severity (workflow-impacting but not blocking), not Information (merely helpful) or Error (required to unblock).
3. Places the banner at the **top of the affected component** (the workspace view / tool window / tab).
4. Keeps the banner text ≤2 sentences and actions ≤2.
5. Uses Jewel `InlineBanner` (component-attached) over `DefaultBanner` for inline contextual use.

## Pass criteria

- [ ] Recommends `InlineBanner` (or `DefaultBanner` with justification) rather than a `Tooltip`, plain `Text`, `Dialog`, or `Notification`.
- [ ] Picks **Warning** severity explicitly — not Information or Error.
- [ ] Specifies placement at the top of the affected component / workspace view.
- [ ] Keeps the copy concise (≤2 sentences) and action count low (≤2 actions); or calls out those limits explicitly.

## Notes

Tests whether the skill distinguishes banner severity levels (Information / Warning / Error) and knows the placement rule (top of affected component). The prompt is intentionally ambiguous about severity — the "before making edits but not blocking" phrasing fits Warning, not Error or Information.

Source: [Banner guideline](https://plugins.jetbrains.com/docs/intellij/banner.html).
