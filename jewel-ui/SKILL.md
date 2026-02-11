---
name: jewel-ui
description: Build or modify Compose Desktop UI using JetBrains Jewel components, theming, and icon loading. Use when requests mention Jewel, IntUiTheme, SwingBridgeTheme, AllIconsKeys, IconKey, PainterHint, or migration from Material/Compose widgets to Jewel in either standalone apps or IntelliJ Platform plugins.
---

# Jewel UI

Implement UI with Jewel by first selecting the runtime context, then applying the correct theme wrapper, then using Jewel components and icon APIs.

## Quick Snippets

Standalone:

```kotlin
IntUiTheme(isDark = false) {
    App()
}
```

IntelliJ plugin:

```kotlin
SwingBridgeTheme {
    App()
}
```

Icon loading:

```kotlin
object MyIcons {
    val Settings = PathIconKey("icons/settings.svg", MyIcons::class.java)
}

Icon(key = MyIcons.Settings, contentDescription = "Settings")
```

## Classify Runtime Context

Decide runtime before writing code:

1. IntelliJ Platform plugin: use the Swing bridge (`SwingBridgeTheme`) and IntelliJ bundled modules.
2. Standalone Compose Desktop app: use `IntUiTheme` and standalone Jewel dependencies.

If context is unclear, inspect build files and imports first:
- `org.jetbrains.jewel.bridge.theme.SwingBridgeTheme` implies plugin context.
- `org.jetbrains.jewel.intui.standalone.theme.IntUiTheme` implies standalone context.

Use [STANDALONE-VS-BRIDGE.md](STANDALONE-VS-BRIDGE.md) for dependency and wrapper snippets.

## Apply Theming Correctly

Use the simplest valid theme API first:

1. Standalone quick start: `IntUiTheme(isDark = ...)`.
2. Standalone advanced: `IntUiTheme(theme = ..., styling = ..., swingCompatMode = ...)`.
3. IntelliJ plugin: `SwingBridgeTheme { ... }`.

When implementing custom standalone themes:

1. Build `ThemeDefinition` via `JewelTheme.lightThemeDefinition(...)` or `JewelTheme.darkThemeDefinition(...)`.
2. Override text styles using `JewelTheme.createDefaultTextStyle()` and `JewelTheme.createEditorTextStyle()`.
3. Pass composed styling through `ComponentStyling.default().with(...)` (or specialized style builders).
4. Prefer public API packages; avoid internal/experimental APIs unless explicitly required.

Use [THEMING.md](THEMING.md) for concrete patterns.
Use [THEMING-COLORS.md](THEMING-COLORS.md) for color-palette and semantic-color guidance.
Use [TYPOGRAPHY.md](TYPOGRAPHY.md) for text-style guidance and when-to-use rules.

## Build UI With Jewel Components

Prefer Jewel components from `org.jetbrains.jewel.ui.component` over Material equivalents.

When converting existing UI:

1. Keep layout containers from Compose where appropriate.
2. Replace controls with Jewel controls (`Button`, `TextField`, `Checkbox`, `Tabs`, etc.).
3. Keep style access through Jewel theme locals and component styling APIs instead of hardcoded colors.

Use local samples as source-of-truth examples:
- [showcase sample directory](https://github.com/JetBrains/intellij-community/tree/master/platform/jewel/samples/showcase)
- [standalone sample directory](https://github.com/JetBrains/intellij-community/tree/master/platform/jewel/samples/standalone)

Use [LAYOUT-PATTERNS.md](LAYOUT-PATTERNS.md) for composition archetypes extracted from those sample apps.
Use [COMPONENTS-CATALOG.md](COMPONENTS-CATALOG.md) for component-by-component catalog guidance.

## Load Icons The Jewel Way

Use `IconKey`-based loading for portability across standalone and bridge:

1. Use `PathIconKey(path, iconClass)` when icon path is the same across old/new UI.
2. Use `IntelliJIconKey(oldUiPath, newUiPath, iconClass)` when paths differ.
3. Use `Icon(key = ..., contentDescription = ...)` or `Image(iconKey = ...)` instead of deprecated raw `painterResource`.
4. Use `AllIconsKeys` for IntelliJ platform icons.

When using `AllIconsKeys` in standalone apps, ensure IntelliJ icons are on classpath (recommended: `com.jetbrains.intellij.platform:icons`).

Use `PainterHint` only when stateful/dynamic path or runtime icon patching behavior is required.

Use [ICONS.md](ICONS.md) for icon patterns and pitfalls.

## Source Permalinks

When citing source in responses, prefer `master` links for always-latest behavior:

- [README.md (standalone, bridge, icons)](https://github.com/JetBrains/intellij-community/blob/master/platform/jewel/README.md#L193-L389)
- [standalone sample main](https://github.com/JetBrains/intellij-community/blob/master/platform/jewel/samples/standalone/src/main/kotlin/org/jetbrains/jewel/samples/standalone/Main.kt#L36-L84)
- [Icon API (`Icon` composable)](https://github.com/JetBrains/intellij-community/blob/master/platform/jewel/ui/src/main/kotlin/org/jetbrains/jewel/ui/component/Icon.kt#L55-L160)
- [Icon key types](https://github.com/JetBrains/intellij-community/blob/master/platform/jewel/ui/src/main/kotlin/org/jetbrains/jewel/ui/icon/IconKey.kt#L5-L73)
- [IntUiTheme implementation](https://github.com/JetBrains/intellij-community/blob/master/platform/jewel/int-ui/int-ui-standalone/src/main/kotlin/org/jetbrains/jewel/intui/standalone/theme/IntUiTheme.kt#L862-L902)

## Version Discipline

Treat this skill as Jewel-version scoped.

1. Ask for target Jewel version and target IntelliJ Platform version when not specified.
2. Validate compatibility against [Jewel release notes](https://github.com/JetBrains/intellij-community/blob/master/platform/jewel/RELEASE%20NOTES.md).
3. Prefer APIs available in the target version; avoid suggesting newer APIs without stating the minimum version.
4. If publishing a version-pinned variant of this skill, replace `master` links with release-tag links.

## Implementation Checklist

Before finishing:

1. Confirm context-specific theme wrapper is correct (`IntUiTheme` vs `SwingBridgeTheme`).
2. Confirm icon code uses `IconKey` and classpath-friendly resource resolution.
3. Confirm dependencies match context.
4. Confirm no unnecessary Material dependency is introduced in standalone flows.
5. Confirm code compiles with current module and imports.

## Related Skill

For deep Compose-in-Swing integration flows (tool windows, ComposePanel wrappers, compositing flags, AWT bridging), use `jewel-swing-interop`.
