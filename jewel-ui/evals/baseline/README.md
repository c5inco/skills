# Baseline: frozen skill snapshot

Frozen copy of the `jewel-ui` skill as it existed at commit `d5b33c4` ("Add COMPONENT-SELECTION reference and Tier 3 compositional evals"). This is the post-Tier-3 state — absolute corpus score ~98% on the 13-prompt corpus — and serves as the comparison point for runs starting with **run 8**.

## Purpose

Used for A/B comparison against ongoing work. Run eval prompts (`../01-*.md` onward) against both this baseline and the current `jewel-ui/` skill; diff the responses to judge whether new changes improved, regressed, or held parity.

## Historical baselines

Previous snapshots (per git history; no longer stored in-tree):

- **`df174ec`** — original baseline for runs 1–7. Captured the pre-session state before any eval-driven edits. All deltas in `../RESULTS.md` runs 1–7 are measured against that snapshot. `git show df174ec:jewel-ui/<file>` reconstructs it if needed.

## Using this snapshot

When running an eval against the baseline, point the model at these files only — do not let it read the top-level `jewel-ui/` skill, or the comparison is invalidated.

## Do not edit

Treat this as read-only. When this snapshot is superseded by a new milestone, overwrite it with the new state and update the commit SHA / date above in a single commit.
