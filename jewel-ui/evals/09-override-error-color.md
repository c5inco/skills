---
id: 09-override-error-color
category: howto
difficulty: hard
---

## Prompt

> Override the global error color in my Jewel theme.

## Expected skill behavior

1. Routes to THEMING-COLORS.md "Overriding Color Systems" section.
2. Uses `GlobalColors.light(...)` / `GlobalColors.dark(...)` factory.
3. Overrides error tokens on both `TextColors` (e.g. `error`) and `OutlineColors` (e.g. `error`, `focusedError`) to keep state coherent — per the guidance that "text, border, and outline should communicate the same state."
4. Wires the custom `GlobalColors` into `lightThemeDefinition` / `darkThemeDefinition` via the `colors =` parameter.
5. Passes the theme definition into `IntUiTheme(theme = ...)`.

## Pass criteria

- [ ] Uses `GlobalColors.light(...)` or `GlobalColors.dark(...)` factory (not per-call inline overrides).
- [ ] Overrides error on **both** `TextColors` and `OutlineColors` for coherent state (not just one).
- [ ] Wires the customized `GlobalColors` into a `ThemeDefinition` (via `lightThemeDefinition(colors = ...)` / `darkThemeDefinition(colors = ...)`).
- [ ] Passes the `ThemeDefinition` into `IntUiTheme(theme = ..., styling = ...)`.
- [ ] Does not recommend hardcoding the error color at `Text(color = ...)` call sites as the solution.
