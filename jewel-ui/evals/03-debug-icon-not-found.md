---
id: 03-debug-icon-not-found
category: debug
difficulty: medium
---

## Prompt

> I'm getting "icon not found" errors in my Jewel UI. What am I missing?

## Expected skill behavior

1. Points to ICONS.md "Common pitfalls" section.
2. Enumerates likely causes: wrong `iconClass`, missing classpath resource, standalone app missing `AllIconsKeys` dependency.
3. Asks or checks context (standalone vs plugin) because the `AllIconsKeys` fix differs.

## Pass criteria

- [ ] Mentions checking that `iconClass` matches the classloader containing the resource.
- [ ] Mentions verifying the resource path exists on classpath at build time.
- [ ] For standalone context, mentions `com.jetbrains.intellij.platform:icons` dependency when using `AllIconsKeys`.
- [ ] Asks to clarify runtime context (standalone vs plugin) if unclear from the prompt.
- [ ] Does not suggest `painterResource` as a workaround.
