---
id: 15-input-field-placeholder-antipattern
category: howto
difficulty: medium
---

## Prompt

> Show me a text field where the placeholder says "Search users".

## Expected skill behavior

1. Routes to LABEL-RULES.md "Writing Component Labels" rules or spots the placeholder-as-label anti-pattern.
2. Pushes back on placeholder-as-label — the user's framing treats the placeholder as carrying the field's purpose, which the IntelliJ guideline rejects.
3. Pairs the field with an explicit visible label ("Users" or similar) and uses the placeholder only for example input.
4. Uses Jewel `TextField`.
5. Notes that placeholders hide on typing (not focus) — so they can't carry long-term meaning.

## Pass criteria

- [ ] Pairs the `TextField` with a visible label (e.g. a `Text` or `GroupHeader` above/beside it), not a placeholder carrying the label role.
- [ ] Placeholder content is an example input (e.g. "name or email") rather than the field's identity ("Search users").
- [ ] Explicitly addresses or flags the placeholder-as-label anti-pattern (cites the rule or explains why it matters for accessibility / when the user types).
- [ ] Uses Jewel's `TextField` (not a hand-rolled control, not Material).

## Notes

This eval tests whether the skill catches the anti-pattern in the user's own framing — the prompt *assumes* the placeholder carries meaning ("placeholder says 'Search users'"), which is the wrong model. The right response corrects it.

Source: [Input Field guideline](https://plugins.jetbrains.com/docs/intellij/input-field.html).
