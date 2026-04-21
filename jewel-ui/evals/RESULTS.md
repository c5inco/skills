# Eval Results

Per-run eval results for the `jewel-ui` skill. Newest run on top.

## Format

Each run gets a section:

```
## <run-label> — <YYYY-MM-DD>

| Prompt | Pass | Notes |
|---|---|---|
| 01 login form | 5/6 | missed: TextField overload disambiguation |
| 02 svg icon | 5/5 | |
| 03 icon not found | 4/5 | did not ask to clarify runtime context |
| 04 intui vs bridge | 4/4 | |
```

- **Run label**: `current @ <short-sha>` for the live skill, `baseline @ cb537ec` for the frozen snapshot. If the baseline rolls forward, update the SHA.
- **Date**: when the run was executed, not when the skill was authored.
- **Pass**: `<satisfied>/<total>` of the prompt's pass-criteria checkboxes.
- **Notes**: one line per run per prompt. Lead with what was missed; "—" if fully passing.

Split this file by quarter if the corpus grows past ~20 prompts or ~20 runs.

## Runs

## run 7 — Tier 3 compositional taste (evals 11–13) — 2026-04-21

Tests whether the skill picks the *right* component for a UX intent, not just any technically-correct one. Added `COMPONENT-SELECTION.md` (decision-tree reference grounded in the JetBrains IntelliJ UI Guidelines) and a short "Pick the Right Component" section in SKILL.md that cross-links to it. Three new prompts exercise three common traps.

### current — evals 11/12/13

| Prompt | Pass | Notes |
|---|---|---|
| 11 subscription tier form | **6/6** | `RadioButtonRow` for 3 tiers, single-enum state, `GroupHeader("Subscription tier:")` with colon, `DefaultButton` + `OutlinedButton` footer. Explicitly cited the guideline rule ("never two primary buttons side by side") |
| 12 confirm-delete dialog | 5/5 | `DefaultButton("Delete")` + `OutlinedButton("Cancel")`. Flagged the "Do not show again" exception to the no-negation rule — extra credit |
| 13 settings toggles | 5/5 | `CheckboxRow` column, `GroupHeader("Display:")` / `GroupHeader("Files:")` with colons, explicit "avoid negation — write 'Show line numbers' not 'Hide line numbers'" |

Total: **16/16**.

### baseline — evals 11/12/13

| Prompt | Pass | Notes |
|---|---|---|
| 11 subscription tier form | 5/6 | Picked `RadioButtonRow` correctly, single-enum state, but `GroupHeader("Subscription tier")` is missing the `:` — the Jewel/IntelliJ label rule isn't in baseline's corpus |
| 12 confirm-delete dialog | 5/5 | Correct primary/secondary assignment in the main code sample. Did suggest an "if you want to emphasize the destructive nature, swap so Cancel is `DefaultButton`" alternative — borderline against the IntelliJ rule, but the primary answer is correct |
| 13 settings toggles | 5/5 | `CheckboxRow` column, `GroupHeader` sections (without colon), imperative labels. Structurally matches current — the colon rule doesn't surface in this prompt's criteria |

Total: **15/16**.

### Observations

- **Net delta: +1, on eval 11's `GroupHeader` colon rule.** That's the specific Jewel/IntelliJ label convention that isn't broadly-known Compose knowledge — it's the kind of detail only a guidelines-grounded reference can reliably surface.
- **Component picks were strong on both versions.** Both current and baseline reached for `RadioButtonRow`, `DefaultButton`+`OutlinedButton`, and `CheckboxRow` unprompted. The model's general UX knowledge covers the headline "pick the right control" decisions; the skill's value is in the *details* (labels, grouping, state shape).
- **Quality gain is larger than the score gain.** Current's eval 11 response explicitly cited why — "never two primary buttons side by side", "the one place Jewel's 'no trailing punctuation' rule intentionally inverts", guidance on what to do if tiers grow past 4. Baseline gave a correct answer without that vocabulary. The pass-criteria count understates the teaching-value delta.
- **Eval 12 baseline had a borderline suggestion.** It recommended swapping so Cancel becomes the `DefaultButton` "to emphasize the destructive nature" — that's the opposite of the IntelliJ rule. The primary code sample was correct so the criteria still pass, but the alternative suggestion is a real confusion that current avoided by citing the rule directly.

### Follow-ups

- **Add more label-rule prompts to probe the gap further.** Something like *"Write the label for a checkbox that disables email notifications"* would cleanly hit the no-negation rule (baseline might write "Don't send me emails"; current should write "Email notifications" and let "off" mean off, or switch to radio).
- **Consider also pulling Button and Group Header guideline pages** — we cited them in COMPONENT-SELECTION.md but didn't read them. They'd tighten evals 12 and 11 respectively.
- **`CheckboxRow` label coloning isn't surfacing in eval 13.** Current passed but didn't explicitly cite the rule for CheckboxRow labels. Could add a small eval that directly tests label rules across radio + checkbox + combo box on a single prompt.

## run 6 — eval 08 after Decorated Window snippet — 2026-04-21

Closed the run-5 shared gap by adding a Decorated Window Quick Snippet to SKILL.md and strengthening THEMING.md's "Decorated window styling" section with explicit *"customization happens through `TitleBarStyle`, not through `IntUiTheme(isDark = ...)` alone"* language. Three current-skill samples against prompt 08 only (baseline unchanged).

### current-v2 — eval 08 × 3 samples

| # | Pass | `titleBarStyle` via `ComponentStyling.default().decoratedWindow(...)`? |
|---|---|---|
| sample 1 | **5/5** | yes — light/dark swap wired |
| sample 2 | **5/5** | yes — clean form |
| sample 3 | **5/5** | yes — light/dark swap wired |

**n=3, mean 5.0/5, range 5–5.**

### Comparison

| Cohort | n | Mean |
|---|---|---|
| baseline | 1 | 4/5 |
| current (pre-snippet, run 5) | 1 | 4/5 |
| **current-v2** | **3** | **5.0/5** |

### Conclusions

- **Gap closed.** The Quick Snippet + directive THEMING.md language flipped all 3 samples to include `TitleBarStyle` configuration through `ComponentStyling.default().decoratedWindow(...)`. Same pattern as eval 06's win: the fix was *directive* wording ("customization happens through X, not Y alone"), not just adding information.
- **Meta-leak continues to appear occasionally.** Sample 3 included a "References" block listing local file paths despite the harness instruction. Not worth a skill change — if it becomes a pattern, tighten the harness prompt.

## run 5 — Tier 2 expansion (evals 08–10) — 2026-04-21

Coverage expansion into areas the Tier 1 corpus didn't exercise: `DecoratedWindow` custom title bar (08), global color overrides (09), and `AllIconsKeys` availability in standalone (10).

### current — evals 08/09/10

| Prompt | Pass | Notes |
|---|---|---|
| 08 custom title bar | 4/5 | Uses `DecoratedWindow` + `TitleBar`, correct dep, `IntUiTheme`. Misses the `ComponentStyling.default().decoratedWindow(titleBarStyle = ...)` configuration — wraps with `IntUiTheme(isDark = false)` instead of the advanced form from THEMING.md |
| 09 error color override | 5/5 | Exemplary — factory usage, both `TextColors` and `OutlineColors` (with `focusedError`), correct theme-definition wiring, also flagged the `SwingBridgeTheme` non-applicability |
| 10 AllIconsKeys in standalone | 4/4 | "Yes with conditions"; names the dependency and repository requirement |

Total: **13/14**.

### baseline — evals 08/09/10

| Prompt | Pass | Notes |
|---|---|---|
| 08 custom title bar | 4/5 | Same shape as current — misses `TitleBarStyle` configuration |
| 09 error color override | 5/5 | Same shape as current |
| 10 AllIconsKeys in standalone | 4/4 | Same shape as current |

Total: **13/14**.

### Observations

- **No delta on Tier 2.** The edits in this session didn't touch the THEMING-COLORS / ICONS content tested here, so parity is expected.
- **Shared gap on eval 08** — both versions skip the `ComponentStyling.default().decoratedWindow(titleBarStyle = ...)` configuration. This is real (THEMING.md documents the pattern) and worth closing. A short SKILL.md Quick Snippet for decorated-window, or a stronger "when customizing, use this form" note in THEMING.md, would likely surface it.
- **Eval 09 is a high-water mark** — the response quality is exactly what the skill was designed to produce, including a defensive note that this doesn't apply in plugin context.
- **Meta leak on eval 08 current** — response appended a "Relevant files I used for this answer" footer despite the explicit "no meta-commentary" instruction. Cosmetic, doesn't affect scoring; worth watching if it recurs across prompts.

### Cross-run picture

Single-sample-per-prompt tallies across the 10-prompt corpus (using run-4 mean for eval 06):

| | current | baseline |
|---|---|---|
| Evals 01–10 | **~45/47** | **~41.5/47** |
| % | 95.7% | 88.3% |

Wins are concentrated on: 01 (TextField overload note), 03 (context-asking edit), 06 (hardened scope boundary). Tier 2 prompts landed on parity, confirming those areas were already well-covered pre-edit.

### Follow-ups

- **Close eval 08 gap** — consider adding a short decorated-window Quick Snippet to SKILL.md showing `ComponentStyling.default().decoratedWindow(titleBarStyle = ...)` so the customization path is visible without opening THEMING.md. Low-effort; likely closes the shared gap on both versions' behavior.
- **Monitor meta-leak** — if "Relevant files I used" appears in more samples, consider tightening the harness prompt rather than the skill.

## run 4 — eval 06 after hardened scope boundary — 2026-04-21

SKILL.md got a new **Scope Boundary** section near the top (directive: *"the correct response is to name `jewel-swing-interop` explicitly as the skill for that work and stop. Do not walk through `ToolWindowFactory` / `ComposePanel` / `plugin.xml` setup here, even if you know how"*). The soft "Related Skill" footer was removed. Three current-skill samples against prompt 06 only (baseline unchanged → not re-run).

### current-hardened — eval 06 × 3 samples

| # | Pass | Named `jewel-swing-interop`? | Deferred on walkthrough? |
|---|---|---|---|
| sample 1 | **4/4** | yes (×2) | yes — no `ToolWindowFactory` / `ComposePanel` / `plugin.xml` |
| sample 2 | **4/4** | yes (×2) | yes |
| sample 3 | **4/4** | yes (×2) | yes — explicitly "I'll point you there rather than walk through mechanics here" |

**n=3, mean 4.0/4, range 4–4.**

### Comparison

| Cohort | n | Mean | Range |
|---|---|---|---|
| baseline | 4 | 2.5/4 | 2–4 |
| current (pre-hardening) | 4 | 2.5/4 | 2–3 |
| **current-hardened** | **3** | **4.0/4** | **4–4** |

### Conclusions

- **Directive wording worked.** The hardened Scope Boundary flipped all 3 samples to clean 4/4. Both the "name `jewel-swing-interop` explicitly" and "don't walk through embedding" criteria now pass reliably. The in-scope content (`SwingBridgeTheme`, bundled-module deps, icons) is preserved — the samples still answer the theming half of the question.
- **The difference was directive language, not the pointer location.** Earlier current and baseline both *had* a pointer; what changed is imperative framing: "and stop", "do not walk through ... even if you know how". Soft "use jewel-swing-interop" gets treated as supplementary info; hard "do not answer embedding questions from this skill" changes behavior.
- **n=3 is small but the effect is large enough to be real.** Previous variance on this prompt was 2–4; now it's 4–4 with tight clustering. Worth a couple more samples over time to confirm stability, but no further action needed now.

### Follow-ups

- Run 2's eval 06 "regression" is formally closed — it was variance.
- Consider applying the same hardening pattern (directive + imperative) to any other cross-skill boundary if we add more skills that could overlap (none currently).

## run 3 — eval 06 variance probe — 2026-04-21

Three additional samples per version against prompt 06 only, to test whether run 2's "regression" was agent variance.

### current — eval 06 × 3 samples

| # | Pass | Named `jewel-swing-interop`? | Deferred on walkthrough? |
|---|---|---|---|
| sample 2 | 2/4 | no ("Compose-in-Swing interop") | no (full `ToolWindowFactory`) |
| sample 3 | 3/4 | yes | no |
| sample 4 | 3/4 | yes | no |

Combined with run 2's sample 1 (2/4): **n=4, mean 2.5/4, range 2–3**.

### baseline — eval 06 × 3 samples

| # | Pass | Named `jewel-swing-interop`? | Deferred on walkthrough? |
|---|---|---|---|
| sample 2 | 2/4 | no ("dedicated Compose-Swing interop skill") | no |
| sample 3 | 2/4 | no | no |
| sample 4 | 2/4 | no | no |

Combined with run 2's sample 1 (4/4): **n=4, mean 2.5/4, range 2–4**.

### Conclusions

- **No regression.** Current and baseline score identically on eval 06 over 4 samples each (mean 2.5/4). Run 2's 4/4 baseline was a lucky draw — baseline actually varies more than current on this prompt.
- **Both versions have a real skill gap.** *Every sample across both versions* failed criterion 3 ("defers to the interop skill") — the model consistently walks through the full `ToolWindowFactory` + `ComposePanel` + `plugin.xml` pattern rather than pointing at `jewel-swing-interop`. Current is slightly better at naming the skill explicitly (2/3 vs 0/3 in this batch), which is consistent with the description-level boundary pointer having *some* effect, just not enough to change the deferral behavior.
- **The criterion may also be too strict.** The full walkthrough is probably useful to the user even if it structurally "belongs" in the interop skill. If we keep the criterion, the skill needs a more directive boundary (e.g. "answer only by pointing to `jewel-swing-interop` — do not walk through embedding here"). If we relax the criterion, we accept that any skill touching the `jewel-ui`/`jewel-swing-interop` seam will answer both halves.

### Suggested follow-ups

1. **Decide the eval 06 criterion.** Keep strict (→ harden SKILL.md boundary language) or relax (→ accept that walkthroughs coexist with the interop-skill pointer). My preference: keep strict and harden the boundary, since the redundancy across skills will compound over time.
2. **Close the "06 regressed" finding** in run 2 — it was variance, not a regression.

## current @ WIP (post-df174ec + context-asking edit) — 2026-04-21 (run 2)

Re-runs eval 03 to validate the SKILL.md context-asking edit; adds new evals 05/06/07.

| Prompt | Pass | Notes |
|---|---|---|
| 03 icon not found | **5/5** ↑ | SKILL.md edit worked — response now explicitly asks "standalone plugin or standalone Compose Desktop app?" before narrowing |
| 05 font rendering | 4/4 | Leads with JBR as root cause; gives actionable toolchain fix |
| 06 Compose in tool window | **2/4** ↓ | Regression vs baseline — gave full `ToolWindowFactory` + `ComposePanel` + `plugin.xml` walkthrough, and referenced "Compose-in-Swing interop flow" without naming `jewel-swing-interop` |
| 07 disable button | 4/4 | Directly answers with `enabled = false`; no version gating |

Total for this run's prompts: **15/17**.

## baseline @ df174ec — 2026-04-21 (run 2)

| Prompt | Pass | Notes |
|---|---|---|
| 03 icon not found | 4/5 | Same gap as run 1 — did not ask for runtime context |
| 05 font rendering | 4/4 | Leads with JBR; fix is correct. JBR info was already discoverable in baseline's STANDALONE-VS-BRIDGE.md — the current-skill checklist addition didn't change observable behavior here |
| 06 Compose in tool window | 4/4 | Explicitly names `jewel-swing-interop` as the companion skill; defers on the `ToolWindowFactory` walkthrough |
| 07 disable button | 4/4 | Same behavior as current |

Total for this run's prompts: **16/17**.

### Run-pair observations

- **Win confirmed** — context-asking edit on eval 03 flipped the response from generic triage to an explicit runtime-context question, closing the criterion gap. This is exactly what the edit was designed to do.
- **Surprise regression on 06** — current underperformed baseline. Possible causes:
  1. Agent-run variance (one sample per cell).
  2. The description-level boundary pointer to `jewel-swing-interop` plus the `LAYOUT-PATTERNS.md` cross-ref may be read as "this skill owns the basics, the other owns depth" — pushing the model to attempt a walkthrough rather than defer outright.
  3. Baseline's "Related Skill" callout at the *bottom* of SKILL.md happens to be more directive in practice than a description-level hint.
- **Eval 05 and 07 pass on both versions** — JBR info (05) was discoverable pre-edit; `enabled = false` (07) is a Compose convention the model reaches for regardless of skill content.
- **Net delta across both prompt sets (2026-04-21 runs 1+2):** current scores **34/37**, baseline scores **34/37** — the eval 03 gain is cancelled by the eval 06 loss.

### Follow-ups

- Re-run eval 06 once or twice more to rule out agent variance before changing the skill.
- If the regression holds, consider strengthening SKILL.md's boundary language — something more directive than "use jewel-swing-interop" (e.g. "for tool-window embedding and `ComposePanel` wiring, answer only by pointing to `jewel-swing-interop`; do not walk through it here").

## current @ WIP (post-df174ec, uncommitted) — 2026-04-21 (run 1)

| Prompt | Pass | Notes |
|---|---|---|
| 01 login form | 6/6 | — |
| 02 svg icon | 5/5 | — |
| 03 icon not found | 4/5 | did not ask user to clarify runtime context; handled both inline |
| 04 intui vs bridge | 4/4 | — |

Total: **19/20**.

## baseline @ df174ec — 2026-04-21

| Prompt | Pass | Notes |
|---|---|---|
| 01 login form | 5/6 | TextField shown only with `state = ...` overload; no `value`/`onValueChange` disambiguation |
| 02 svg icon | 5/5 | — |
| 03 icon not found | 4/5 | did not ask user to clarify runtime context; uses "deprecated" phrasing for `painterResource` |
| 04 intui vs bridge | 4/4 | — |

Total: **18/20**.

### Run-pair observations

- Delta of **+1** on eval 01 is directly attributable to the `TextField` overload note added to `COMPONENTS-CATALOG.md`.
- Eval 03 loses a point on both versions for the same criterion ("Asks to clarify runtime context"). Both responses covered standalone *and* plugin cases inline instead of asking. Open question: tighten the skill to prompt for context, or relax the criterion since handling both is arguably better UX.
- The `painterResource` phrasing fix in `ICONS.md` shows up in eval 02/03 current responses (accurate "bypasses pipeline" framing) but didn't affect pass/fail — pure quality improvement.
- Other edits in this batch (trigger description broadening, JBR checklist item, Version Discipline softening, Pattern 6 cross-ref, line-range stripping) had no observable impact on this 4-prompt corpus — they target areas not exercised here.
