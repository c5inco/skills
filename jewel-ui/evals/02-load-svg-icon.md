---
id: 02-load-svg-icon
category: howto
difficulty: easy
---

## Prompt

> How do I load an SVG icon that's in my plugin resources?

## Expected skill behavior

1. Points to ICONS.md for icon loading patterns.
2. Recommends `PathIconKey` or `IntelliJIconKey` based on old/new UI path symmetry.
3. Shows an icon holder object pattern (`object MyIcons { val Settings = PathIconKey(...) }`).
4. Uses `Icon(key = ..., contentDescription = ...)` at the call site.

## Pass criteria

- [ ] Recommends `IconKey`-based API, not raw `painterResource`.
- [ ] Shows a holder object grouping icon keys.
- [ ] Passes the correct `iconClass` (second argument to `PathIconKey`) so the classloader can resolve the resource.
- [ ] Includes a non-empty `contentDescription` (or explicit `null` with a reason).
- [ ] Notes that icon resources must be on classpath under the path used in the key.
