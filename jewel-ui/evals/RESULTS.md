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
