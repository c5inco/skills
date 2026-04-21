---
id: 08-custom-title-bar
category: howto
difficulty: medium
---

## Prompt

> I want a custom title bar in my standalone Jewel app.

## Expected skill behavior

1. Routes to THEMING.md "Decorated window styling (standalone)" section.
2. Recommends `DecoratedWindow` + `TitleBar` composables.
3. Shows `ComponentStyling.default().decoratedWindow(titleBarStyle = TitleBarStyle.light())`.
4. Mentions the `jewel-int-ui-decorated-window` dependency is required.
5. Keeps the answer in standalone context (`IntUiTheme`).

## Pass criteria

- [ ] Uses the `DecoratedWindow` composable.
- [ ] Shows `TitleBarStyle` configured via `ComponentStyling.default().decoratedWindow(...)`.
- [ ] Mentions the `jewel-int-ui-decorated-window` artifact / dependency.
- [ ] Uses `IntUiTheme` (not `SwingBridgeTheme`) — this is a standalone-only feature.
- [ ] Does not suggest plugin-specific APIs (e.g. IntelliJ Platform tool-window chrome).
