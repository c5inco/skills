---
id: 04-intui-vs-swingbridge
category: explain
difficulty: easy
---

## Prompt

> What's the difference between `IntUiTheme` and `SwingBridgeTheme`? When do I use which?

## Expected skill behavior

1. Points to SKILL.md "Classify Runtime Context" and STANDALONE-VS-BRIDGE.md.
2. States the runtime mapping: `IntUiTheme` for standalone Compose Desktop, `SwingBridgeTheme` for IntelliJ Platform plugins.
3. Explains that `SwingBridgeTheme` pulls Swing LaF values (colors, typography, metrics, icon behavior) into Compose; `IntUiTheme` supplies them from standalone Int UI defaults.
4. Mentions dependency differences (standalone artifact vs IntelliJ bundled modules).

## Pass criteria

- [ ] Correctly maps `IntUiTheme` → standalone, `SwingBridgeTheme` → plugin.
- [ ] Explains what the bridge "bridges" (LaF values: colors, typography, metrics, icons).
- [ ] Notes that dependencies differ between the two contexts.
- [ ] Does not recommend `SwingBridgeTheme` for a non-plugin scenario.
