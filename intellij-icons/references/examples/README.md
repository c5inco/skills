# Reference Icons

Real shipped icons that illustrate the rules in `SKILL.md`. Each comes as a
light/dark pair. Read the SVG source to see exact geometry, clearances, and
palette mapping; render it to compare visual weight.

Every file follows the skill's rules exactly, so you can copy geometry and
attributes from them directly. All linework is live strokes. Many shipped
exports outline strokes into filled paths with Figma-style decimals; those were
redrawn as live strokes on the `0.5px` grid and compared against the originals
at 1× and 2×. See [Changes from the shipped icons](#changes-from-the-shipped-icons)
for the few visible differences. The only fills are filled-by-design shapes
(the `warning` badge, the `interface` letterform, tints).

| File | Size | Demonstrates |
| :--- | :--- | :--- |
| `intellij/search.svg` | 16 | Connected glyph with a diagonal: the handle starts inside the lens's stroke at 45° (`10.5 10.5`), so the two strokes overlap with no gap. The 45° handle stays `1px` and renders softer than the lens at 1× — that is expected, not a defect. |
| `intellij/interface.svg` | 16 | Letterform converted to an outlined path (no `<text>`): the serif "I" sits entirely on the `0.5px` grid, inside a Green **Stroke** + **Tint** node circle (`r="6.5"`). |
| `intellij/locate.svg` | 16 | Connected glyph with axis-aligned joins: ticks start inside the ring's stroke at 90°. The ticks sit on the axes of symmetry (`8`), the allowed exception to pixel-aligned strokes. |
| `intellij/close.svg` | 16 | Pure 45° diagonals at `1px` with round caps. Single segments, so no join attribute is needed. |
| `intellij/down.svg` | 16 | Vertical arrow: arms at 45° to the shaft (90° apart), meeting at a round join. The shaft sits on the axis of symmetry (`x="8"`), the allowed exception to pixel-aligned strokes. |
| `intellij/debug.svg` | 16 | Pixel-aligned strokes: the body's sides (`x="4.5"`/`11.5`), the middle legs (`y="9.5"`), and the extremes of the head and body arcs sit on `.5` centerlines, so they render as crisp 1px lines. The legs keep the symbol's canonical shallow angle (2:1). |
| `intellij/export.svg` | 16 | Diagonal arrow: 45° shaft with one horizontal and one vertical arm, beside an open bracket with a `1.5` arc corner. |
| `intellij/openInToolWindow.svg` | 16 | Diagonal arrow as live strokes with round caps/joins inside an inner-stroke frame (`x="2.5"`, `rx="1.5"` → `2px` visible radius). |
| `intellij/restartStop.svg` | 16 | Stop modifier, bottom-right, using Red **Stroke** + **Tint**. The restart arc is cut flat by a `<clipPath>` along the `1px` clearance contour (a rounded square around the modifier) instead of ending in a round cap. |
| `studio/layout-inspector.svg` | 16 | Magnifier modifier in Blue **Accent**; the front card is cut by a `<clipPath>` circle `1px` outside the lens (`r="4"`), so its cut ends follow the lens silhouette. |
| `studio/add-component.svg` | 16 | Green **Accent** (`#369650` / `#57965C`) plus modifier, centered on the bottom edge of a symmetric base; the bottom stroke is interrupted around it instead of painted over. Its ends keep round caps: the interruption is head-on along the stroke's own axis, facing the plus's round ends (the exception in *Cut ends, not caps*). |
| `studio/run-on-device.svg` | 16 | Play modifier with Green **Stroke** + **Tint** on a neutral phone base. The phone outline is cut flat by a rectangular `<clipPath>` at least `1px` from the play triangle, which keeps its canonical angles with vertices on the grid. |
| `studio/run-on-device@14x14.svg` | 14 | The same icon re-authored for `14×14` — compare with the `16×16` version for modifier sizing at 14px. |
| `studio/device-explorer@20x20.svg` | 20 | Magnifier modifier at `20×20`: `1.5` stroke, and a `<clipPath>` circle giving `1.5px` clearance (vs. `1px` in `layout-inspector.svg`). |
| `studio/show-constraints.svg` | 16 | Occluding slash, with the eye's top and bottom on `.5` centerlines (`2.5`/`13.5`): the eye and pupil are cut by a `<clipPath>` band on the slash's upper-right side (one-sided clearance, as in the shipped icon); the lower-left pieces abut the slash. |
| `studio/structure@20x20.svg` | 20 | `20×20` base shapes as live-stroke `<rect>`s: `1.5px` strokes, `2px` outer corner radius (`rx="1.25"`), and the `0.75px` inner-stroke inset (`x="2.75"`), fitted to the `16×16` square keyline (`2..18`). |
| `studio/flag@14x14.svg` | 14 | Simple `14×14` outline with pixel-aligned `.5` `1px` strokes, round caps and joins, and a 45° fold. |
| `studio/warning.svg` | 16 | Yellow **Solid** with **On yellow solid** glyph (`#FFFFFF` light / `#5E4D33` dark). The triangle's same-color stroke rounds its corners while its vertices stay on the grid. |

## Changes from the shipped icons

Raster comparison against the shipped originals (share of painted pixels whose
luminance differs noticeably, at 1× / 2×):

| File | Difference | Why |
| :--- | :--- | :--- |
| `search`, `locate`, `export`, `add-component`, `structure@20x20`, `layout-inspector`, `device-explorer@20x20` | 0% / 0% | Same geometry (and `add-component` uses Green Accent `#369650` on light); only the source changed (live strokes, snapped coordinates, `<clipPath>` cuts). |
| `restartStop` | 4% / 0% | Arc start snapped to the grid. |
| `down` | 9% / 13% | Round join at the tip, as the skill requires; the shipped icon has a sharp miter. Arms snapped `0.2px` lower. |
| `warning` | 10% / 16% | Corner radius `0.5px` (from the round join) instead of about `1.6px`, so the vertices stay on the grid. |
| `run-on-device`, `run-on-device@14x14` | 10% / 17% | Play triangle vertices snapped to the grid. |
| `show-constraints` | 33% / 34% | The eye is narrowed to keep the `1px` outer padding (the shipped eye touches the canvas edges), and its top and bottom moved to `.5` centerlines so they render crisp instead of blurred across two rows. |
| `debug` | 36% / 42% | The shipped body's sides and bottom sit on whole-number centerlines (`x="4"`, `12`, `y="14"`), so they blur across two pixels at 1×. The redraw moves them to `.5` centerlines, making the body `1px` narrower; legs simplified to grid-snapped 2:1 slopes. |
| `flag@14x14` | 36% / 43% | The shipped pole (`x=3.14`), right side (`x=10.79`), and bottom edges sit off `.5` centerlines and blur across pixel columns/rows; snapping all straight strokes to `.5` centerlines makes them crisp. The fold is now 45° instead of about 27°. |

## Sources

- `intellij/`: IntelliJ Platform expui icons, from
  [intellij-icons.web.app](https://intellij-icons.web.app) and
  [JetBrains/intellij-community](https://github.com/JetBrains/intellij-community).
- `studio/`: Android Studio icons, from
  [studio-icons.web.app](https://studio-icons.web.app) and Android Studio
  `artwork`.

Modified files carry a header comment noting the redraw. `close`,
`openInToolWindow`, and `interface` are unmodified. `studio/` files were
renamed to this skill's filename convention (e.g., the gutter
`run-on-device.svg` → `run-on-device@14x14.svg`).
