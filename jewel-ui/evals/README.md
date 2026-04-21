# Jewel UI Skill Evals

Simulated user prompts used to check whether the `jewel-ui` skill produces correct, complete guidance.

## Format

Each eval is a standalone markdown file with:

1. **Frontmatter** — `id`, `category`, `difficulty`.
2. **Prompt** — the verbatim user input being simulated.
3. **Expected skill behavior** — which SKILL.md sections and reference files the response should draw on.
4. **Pass criteria** — observable properties a correct answer must have.
5. **Notes** — known gaps, caveats, or follow-ups.

## Running an eval

Evals are manual for now. Process:

1. Start a fresh conversation pointed at the `jewel-ui` skill.
2. Paste the prompt verbatim.
3. Compare the response against the pass criteria checklist.
4. File gaps as skill updates or new evals.

## A/B comparison against baseline

The `baseline/` subdirectory is a frozen snapshot of the skill from before the current eval-driven edits. Use it to judge whether changes improved the skill:

1. Run a prompt against the current `jewel-ui/` skill; record which pass-criteria boxes the response satisfies.
2. Run the same prompt against `baseline/` in a separate fresh conversation.
3. Diff the two responses against the criteria. Any regression is a blocker; any new box checked is evidence the change helped.

See `baseline/README.md` for the snapshot's provenance and a summary of what's different.

## Process

The iteration loop for keeping the skill, evals, and baseline in sync:

1. **Add prompts freely.** When adding a new eval prompt, run it once against `jewel-ui/` and once against `baseline/`. Record both in `RESULTS.md` so the A/B data point is captured at birth.
2. **Before any skill edit lands, run all evals twice** — current skill and edited skill. A regression on a previously-passing criterion is a blocker; fix or revert before merging.
3. **Roll `baseline/` forward on named milestones, not per-edit.** When you do, update `baseline/README.md` (new commit SHA, date, diff summary) and start the next run section in `RESULTS.md` under the new baseline.
4. **Don't accumulate `baseline-*/` directories** — git handles old snapshots. The in-tree baseline exists only so the current A/B is runnable without branch switching.

Record every run in `RESULTS.md`, newest on top.

## Deferred / Open

Parked items to revisit next cycle:

### Baseline rollforward

The in-tree baseline at `baseline/` currently reflects commit `d5b33c4` (post-Tier-3). After Tier 4 (runs 9–11) stabilized with no regressions on the protected corpus, the natural next step is rolling the baseline forward to the current HEAD. Process is documented above — overwrite `baseline/<files>` with the current `jewel-ui/<files>`, update `baseline/README.md` with the new SHA and a short diff summary, commit as a single named milestone.

### Deferred evals

- **Toggle Button** — IntelliJ scopes "Toggle Button" narrowly to search-result toggles (Swing `OnOffButton`); Jewel has no clean analog. Revisit when Jewel ships an equivalent composable.
- **Search Field** — `COMPONENT-SELECTION.md`'s "Search Affordances" section already encodes the `TextField` + leading icon vs `SpeedSearchArea` differentiation. Add an eval (would be #26) to verify the rule surfaces; good candidate for the next tier.

### Harness note

The A/B harness (`Agent` subagents with explicit file lists) hardcodes which skill `.md` files go to each run. After the Tier 4 split, the current skill spans both `COMPONENT-SELECTION.md` **and** `LABEL-RULES.md` — future A/B runs must include **both** in the current-skill agent's file list, or label rules will be silently missing and any label-rule eval will regress. Baseline runs still read the self-contained `baseline/COMPONENT-SELECTION.md` at the rolled snapshot; update that when rolling baseline forward.

## Difficulty bands

- **easy** — single-section lookup or direct API-name trigger.
- **medium** — multi-step; combines theme + component + icon guidance.
- **hard** — debugging with incomplete info, or reaches into advanced theming, decorated windows, custom styling, or interop edges.

## Categories

- **howto** — "show me how to build X"
- **debug** — "why isn't X working?"
- **explain** — "what's the difference between X and Y?"

## Index

| ID | Category | Difficulty | Prompt summary |
|---|---|---|---|
| [01](01-standalone-login-form.md) | howto | easy | Standalone app + simple login form |
| [02](02-load-svg-icon.md) | howto | easy | Load SVG icon from plugin resources |
| [03](03-debug-icon-not-found.md) | debug | medium | "Icon not found" error triage |
| [04](04-intui-vs-swingbridge.md) | explain | easy | `IntUiTheme` vs `SwingBridgeTheme` |
| [05](05-debug-font-rendering.md) | debug | medium | Standalone app fonts look wrong |
| [06](06-compose-toolwindow-routing.md) | howto | medium | Compose view in an IntelliJ tool window |
| [07](07-disable-button.md) | howto | easy | Disable a Jewel `Button` |
| [08](08-custom-title-bar.md) | howto | medium | Custom title bar in standalone app (`DecoratedWindow`) |
| [09](09-override-error-color.md) | howto | hard | Override global error color in the theme |
| [10](10-allicons-standalone.md) | explain | easy | `AllIconsKeys` in a standalone app |
| [11](11-subscription-tier-form.md) | howto | medium | Form with mutually-exclusive options (radio vs buttons) |
| [12](12-confirm-delete-dialog.md) | howto | easy | Confirm-delete dialog buttons (primary vs secondary) |
| [13](13-settings-toggles.md) | howto | medium | Settings page with ~10 preference toggles |
| [14](14-checkbox-label-negation.md) | howto | medium | Label a checkbox to "disable email notifications" (tests no-negation rule) |
| [15](15-input-field-placeholder-antipattern.md) | howto | medium | Placeholder-as-label anti-pattern ("Search users" as placeholder) |
| [16](16-link-click-here-antipattern.md) | howto | medium | "click here" link text anti-pattern |
| [17](17-tooltip-on-icon-button.md) | howto | medium | Is an `IconButton` with just an icon enough? (tests Tooltip rule) |
| [20](20-textarea-vs-textfield.md) | howto | easy | Commit message input: `TextArea` vs `TextField` |
| [22](22-button-now-antipattern.md) | howto | easy | Button label "Apply Now" vs "Apply" |
| [23](23-groupheader-threshold.md) | howto | medium | 2 checkboxes — use `GroupHeader`? (threshold rule) |
| [18](18-banner-severity-placement.md) | howto | medium | Workspace out-of-sync: which feedback surface + severity? |
| [19](19-progress-bar-determinate.md) | howto | medium | Compile progress: determinate vs indeterminate; background; cancel vs pause |
| [21](21-tabs-at-12.md) | howto | medium | 12 tabs: auto-hide threshold, never-disable rule |
| [24](24-slider-vs-textfield-numeric.md) | howto | medium | Volume 0–100: `Slider` vs `TextField` numeric |
| [25](25-validation-error-presentation.md) | howto | medium | Inline form validation error presentation |
