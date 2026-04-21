---
id: 01-standalone-login-form
category: howto
difficulty: easy
---

## Prompt

> I'm building a standalone Compose Desktop app with Jewel. Show me the theme setup and a simple login form.

## Expected skill behavior

1. Classifies runtime context as standalone via SKILL.md "Classify Runtime Context".
2. Uses `IntUiTheme(isDark = ...)` wrapper.
3. References STANDALONE-VS-BRIDGE.md for dependencies.
4. Pulls form controls (`TextField`, `DefaultButton`, `OutlinedButton`) from COMPONENTS-CATALOG.md.
5. Applies composition guidance from LAYOUT-PATTERNS.md Pattern 4 (vertical control blocks).

## Pass criteria

- [ ] Code uses `IntUiTheme` (not `SwingBridgeTheme`).
- [ ] Dependencies section or note mentions `jewel-int-ui-standalone`.
- [ ] `TextField` usage disambiguates between `TextFieldState` and `value`/`onValueChange` overloads.
- [ ] Buttons use Jewel primitives (`DefaultButton` for primary, `OutlinedButton` for secondary).
- [ ] Layout uses Compose containers with `Arrangement.spacedBy`, not ad-hoc padding.
- [ ] No hardcoded color or font values; uses `JewelTheme` locals when styling is touched.

## Notes

Password obscuring (masked input) is out of scope for this prompt.
