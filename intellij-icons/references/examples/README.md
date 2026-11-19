# Reference Icons

Real shipped icons that illustrate the rules in `SKILL.md`. Each comes as a
light/dark pair. Read the SVG source to see exact geometry, clearances, and
palette mapping; render it to compare visual weight.

These are production exports, so most strokes are already outlined to filled
paths and coordinates carry Figma-style decimals (e.g., `11.475`). Use them as
**design references**, not as models for path hygiene or the `0.5px` snap rule.

| File | Size | Demonstrates |
| :--- | :--- | :--- |
| `intellij/search.svg` | 16 | Connected glyph with a diagonal: the handle starts on the lens's stroke centerline at 45°, so the two strokes overlap with no gap. The 45° handle stays `1px` and renders softer than the lens at 1× — that is expected, not a defect. Authored as live strokes with round caps; light and dark share identical geometry. Its endpoints carry upstream decimals (`10.1992`); when authoring, snap them (e.g., `10.5 10.5`). |
| `intellij/locate.svg` | 16 | Connected glyph with axis-aligned joins: ticks join the ring at 90°, so the joins stay pixel-crisp. |
| `intellij/close.svg` | 16 | Pure 45° diagonals at `1px` with round caps. |
| `intellij/down.svg` | 16 | Vertical arrow: arms at 45° to the shaft (90° apart). Its tip is a sharp miter point — an upstream inconsistency; use a round join instead (see `openInToolWindow.svg`). |
| `intellij/export.svg` | 16 | Diagonal arrow: 45° shaft with one horizontal and one vertical arm. |
| `intellij/openInToolWindow.svg` | 16 | Diagonal arrow as live strokes with round caps/joins inside an inner-stroke frame (`x="2.5"`, `rx="1.5"` → `2px` visible radius). |
| `intellij/restartStop.svg` | 16 | Stop modifier, bottom-right, using Red **Stroke** + **Tint**; base arrow is cut back to leave clearance. |
| `studio/layout-inspector.svg` | 16 | Magnifier modifier in Blue **Accent**; the base rectangle is cut along a circle around the lens, leaving `1px` clearance. |
| `studio/add-component.svg` | 16 | Green plus modifier; the base's bottom stroke is interrupted around it instead of painted over. |
| `studio/run-on-device.svg` | 16 | Play modifier with Green **Stroke** + **Tint** on a neutral phone base. |
| `studio/run-on-device@14x14.svg` | 14 | The same icon re-authored for `14×14` — compare with the `16×16` version for modifier sizing at 14px. |
| `studio/device-explorer@20x20.svg` | 20 | Magnifier modifier at `20×20`: `1.5` stroke, round caps, and `1.5px` clearance (vs. `1px` in `layout-inspector.svg`). |
| `studio/show-constraints.svg` | 16 | Occluding slash: eye strokes are cut around the diagonal so the slash reads cleanly. |
| `studio/structure@20x20.svg` | 20 | `20×20` base shapes: `1.5px` visible strokes, `2px` outer corner radius, fitted to the `16×16` square keyline (`2..18`). |
| `studio/flag@14x14.svg` | 14 | Simple `14×14` outline with `1px` stroke. |
| `studio/warning.svg` | 16 | Yellow **Solid** with **On yellow solid** glyph (`#FFFFFF` light / `#5E4D33` dark). |
| `studio/edit-text.svg` | 16 | Letterforms converted to outlined paths (no `<text>`). |

## Sources & License

- `intellij/`: IntelliJ Platform expui icons, from
  [intellij-icons.web.app](https://intellij-icons.web.app) /
  [JetBrains/intellij-community](https://github.com/JetBrains/intellij-community).
  Copyright JetBrains s.r.o. and contributors, Apache License 2.0.
- `studio/`: Android Studio icons, from
  [studio-icons.web.app](https://studio-icons.web.app) / the Android Open Source
  Project. Apache License 2.0.

Files are unmodified except that `studio/` files were renamed to this skill's
filename convention (e.g., the gutter `run-on-device.svg` →
`run-on-device@14x14.svg`).
