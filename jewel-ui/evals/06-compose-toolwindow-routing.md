---
id: 06-compose-toolwindow-routing
category: howto
difficulty: medium
---

## Prompt

> How do I put a Compose view in an IntelliJ tool window?

## Expected skill behavior

1. Routes to the `jewel-swing-interop` skill per the boundary pointer in SKILL.md's description and the cross-reference in LAYOUT-PATTERNS.md Pattern 6.
2. If any theme wrapper is shown, it is `SwingBridgeTheme` (not `IntUiTheme`).
3. Avoids fully answering the embedding mechanics (`ComposePanel`, `addComposeTab`, `enableNewSwingCompositing`) in this skill — those live in `jewel-swing-interop`.

## Pass criteria

- [ ] Response explicitly mentions `jewel-swing-interop` as the right skill for embedding mechanics.
- [ ] If a theme wrapper is shown, it is `SwingBridgeTheme` (not `IntUiTheme`).
- [ ] Does not give a full `ComposePanel` / `addComposeTab` walkthrough — defers to the interop skill.
- [ ] Does not suggest standalone Jewel dependencies in plugin context.
