---
id: 23-groupheader-threshold
category: howto
difficulty: medium
---

## Prompt

> I have a settings section with 2 checkboxes under a "Display" label. Should I use `GroupHeader`?

## Expected skill behavior

1. Answers: **no** — the IntelliJ Group Header guideline says don't use a group header for ≤3 controls; prefer vertical insets / spacing instead.
2. Explains the reason: small groups scan fine with whitespace; a header adds visual weight without payoff.
3. Suggests what to do instead — vertical `Arrangement.spacedBy`, or fold the 2 checkboxes into the parent section.

## Pass criteria

- [ ] Answers "no" (or pushes back) on using `GroupHeader` here.
- [ ] Cites the threshold rule: headers valuable only for larger groups; ≤3 controls should use spacing instead.
- [ ] Suggests a specific alternative — `Arrangement.spacedBy`, vertical insets/padding, or similar spacing-based separation.
- [ ] Does not propose wrapping each checkbox in its own `Card` or adding a `Divider` between them as a substitute.

## Notes

The prompt invites a default "yes" — `GroupHeader` exists, why not use it? The rule is specifically the lower-bound threshold. Tests whether the skill catches over-structuring for small groups.

Source: [Group Header guideline](https://plugins.jetbrains.com/docs/intellij/group-header.html).
