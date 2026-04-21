# Baseline: pre-change skill snapshot

Frozen copy of the `jewel-ui` skill as it existed at commit `df174ec` ("Update jewel-ui components catalog") — the tip of `main` right before the evaluation-driven edits began in this working tree.

## Purpose

Used for A/B comparison against the current skill. Run the same eval prompts (`../01-*.md` through `../04-*.md`) against this baseline and against the current `jewel-ui/` skill, then diff the answers to judge whether the changes improved coverage, clarity, or correctness.

## What's different in the current skill

Compared to this snapshot, the current `jewel-ui/` skill:

1. Broader trigger description — adds `JewelTheme`, `ComponentStyling`, `DecoratedWindow`, `DefaultButton`, `Tabs`, an intent phrase, and an explicit boundary to `jewel-swing-interop`.
2. No migration framing — description keyword and "Build UI With Jewel Components" subsection reworded away from Material→Jewel migration.
3. Version Discipline softened — "check build files first, ask only if ambiguous" instead of always asking.
4. JBR requirement added to the Implementation Checklist.
5. Accurate `painterResource` phrasing in `ICONS.md` (was: "deprecated").
6. `TextField`/`TextArea` overload disambiguation in `COMPONENTS-CATALOG.md`.
7. `LAYOUT-PATTERNS.md` Pattern 6 cross-references `jewel-swing-interop`.
8. Line-range fragments (`#L…`) stripped from all permalinks to reduce rot.

## Using this snapshot

When running an eval against the baseline, point the model at these files only — do not let it read the top-level `jewel-ui/` skill, or the comparison is invalidated.

One workable approach: copy this directory into a throwaway location, rename it to `jewel-ui/`, and run the eval there.

## Do not edit

Treat this as read-only. If the current skill evolves far enough that a new baseline is useful, add a sibling directory (e.g. `baseline-2026-q2/`) rather than overwriting this one.
