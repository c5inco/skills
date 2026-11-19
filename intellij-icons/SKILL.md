---
name: intellij-icons
description: Creates, audits, and fixes SVG icons in the IntelliJ icon style. Use when asked to review, fix, optimize, rename, or author SVGs following IntelliJ icon guidelines (20x20, 16x16, and 14x14 grids, outline style, stroke weights, corner radii, path hygiene, naming, and light/dark color variants).
---

# IntelliJ Icon Guidelines

Use these rules when creating, auditing, or fixing SVG icons in the **IntelliJ**
style. Section 2 is the single source of truth for per-size values; other
sections reference it rather than repeating them. External or legacy JetBrains
icon docs do not override this skill's stroke, grid, or color values.

## Workflow

- **Authoring a new icon**:
  1. **Find a reference**: Pick the closest icon in
     [`references/examples/README.md`](references/examples/README.md) for the
     technique you need and read its SVG source before drawing.
  2. **Author** at the target size following Sections 1–3 (see Section 5 when
     converting from another icon set).
  3. **Audit** with Section 4 items 1–6.
  4. **Render & inspect** (Section 4 item 7).
  5. **Report** using the Deviation Report format in Section 4.
- **Auditing or fixing an existing icon**:
  1. Run Section 4 items 1–6 (using *Auditing Outlined Files* if strokes are
     outlined).
  2. If asked to fix, apply repairs and re-check the changed items once.
  3. Run Section 4 item 7 and finish with the Deviation Report.

## 1. General Rules

- **Outline first**: Prefer outline icons over filled silhouettes.
- **Flat style**: Keep icons strictly flat — no gradients, drop shadows, blur
  filters, or 3D effects.
- **Minimal detail & clear gaps**: Use the minimum geometry needed to convey
  meaning. Keep at least a `1px` clear gap between parallel strokes (`1.5px` at
  `20×20`) so strokes do not merge at 1×.
- **0.5px minimal step**: Snap coordinates, dimensions, and offsets to `0.5px`
  increments; strip noisy sub-pixel decimals (`3.00012` → `3`, `4.4998` → `4.5`).
  **Exception**: half-stroke-derived values from Section 2 (inner-stroke insets
  and path `rx`) stay exact and must not be re-snapped.
- **Pixel-aligned strokes**: Center horizontal and vertical `1px` strokes — and
  axis-aligned curve extremes — on `.5` coordinates so both painted edges land
  on whole pixels (centerline `4.5` → edges `4` and `5`; whole-number `x="4"`
  blurs across two columns at 1×). At `20×20`, place outer keyline `1.5px`
  strokes on `.25`/`.75` centerlines so their outer edges land on whole pixels;
  `.5` interior centerlines are allowed when needed for symmetric or optical
  spacing (e.g., `studio/structure@20x20.svg`).
  **Axis-of-symmetry exception**: on an even canvas, a stroke on the icon's
  symmetry axis (`x="8"` at `16×16`, `x="10"` at `20×20`, e.g., a vertical arrow
  shaft, plus, or crosshair tick) stays centered on the axis rather than
  shifting off-center; shift by `0.5px` only when the icon is asymmetric.
- **Derived points**: Points fixed by geometric construction (an arc endpoint on
  a concentric circle, a tangent, a regular-polygon vertex) may fall off the
  `0.5px` grid. Compute them exactly, round to two decimals, keep axis-aligned
  edges on the grid, and note the construction (e.g., center and radius) in the
  Deviation Report.
- **Clean path & DOM hygiene**: Remove redundant vertices, collinear points,
  unnecessary curve segments, and unused `<defs>` or `<g>` wrappers.
- **Letterforms**: Use **JetBrains Sans** converted to outlined paths — never
  ship `<text>`. If the font is unavailable, build the glyph from grid-aligned
  geometry matching a catalog letter icon (as in `intellij/interface.svg`) and
  note it in the Deviation Report. Outlined glyph curves are exempt from the
  `0.5px` step; align baseline, cap height, and straight stems to the grid.
- **Exact canvas bounds**: Set `width`, `height`, and `viewBox` to the exact
  icon size (`0 0 16 16`). All painted geometry must stay inside the canvas; use
  a canvas-bounds `<clipPath>` only when a diagonal or curve slightly overhangs
  the edge, never to hide oversized geometry.
- **Avoid masks**: Create cutouts and clearances by cutting path geometry or
  using a `<clipPath>`. Use `<mask>` only when neither is feasible.
- **Unique ids**: Give every `id` (such as a `<clipPath>`) an icon-specific
  name (`layoutInspector-lensClearance`, not `clip`). Light and dark files may
  share the same `id` when their clip geometry is identical; suffix `_dark` if
  clips ever differ.
- **Live strokes, not outlines**: Author and edit linework as stroked paths
  (`stroke="…"`), not outlined filled shapes. `stroke-width="1"` may be omitted
  (SVG default); always set `stroke-width="1.5"` at `20×20`. Use fills only for
  filled-by-design roles: **Solid** badges, **Tint** and **Default fill**
  interiors, and outlined letterforms.

## 2. Size Specifications

Match the SVG canvas size to the UI surface. All sizes use round end caps on
open strokes, round line joins where segments meet, and the same `stroke-width`
for modifiers as for base strokes.

| Property | `20×20` | `16×16` | `14×14` |
| :--- | :--- | :--- | :--- |
| **Usage** | Main toolbar, Tool windows | Default (Toolbars, Trees, Menus, etc.) | Gutter, Status bar |
| **`stroke-width`** | `1.5` | `1` | `1` |
| **Outer padding** (canvas edge to painted geometry) | `1px` | `1px` | `0–1px` |
| **Inner-stroke inset** (`stroke-width / 2`) | `0.75px` | `0.5px` | `0.5px` |
| **Corner radius, large shapes** (visible → path `rx`) | `2px` → `1.25` | `2px` → `1.5` | `1px` → `0.5` |
| **Corner radius, small shapes** (visible → path `rx`) | `1px` → `0.25` | `1px` → `0.5` | `1px` → `0.5` |
| **Modifier visual size** | ~`7.5–11px` | ~`6–9px` | ~`6–9px` |
| **Modifier clearance** | ≥ `1.5px`, typically `1.5–2.5px` | ≥ `1px`, typically `1–2px` | ≥ `1px`, typically `1–2px` |

### Filenames

- **`20×20`**: `name@20x20.svg` / `name@20x20_dark.svg` (both IntelliJ `expui`
  and Android Studio `artwork`).
- **`16×16`**: `name.svg` / `name_dark.svg`.
- **`14×14`**: `name@14x14.svg` / `name@14x14_dark.svg` in IntelliJ `expui` and
  standalone icon sets. In Android Studio `artwork`
  (`tools/adt/idea/artwork/resources/studio/icons/`), `14×14` icons live in
  surface-specific folders (e.g., `gutter-icons/`, `layout-editor/properties/`)
  as `name.svg` / `name_dark.svg` without `@14x14`.
- Follow the target directory's convention, and never rename existing icons in a
  way that breaks references or icon mappings.

### Caps and Joins

Caps and joins are only required where visible (harmless if present on closed or
single-segment paths): open ends take `stroke-linecap="round"`, any vertex where
segments meet (polylines, arrowheads, mixed line/arc paths, closed polygons)
takes `stroke-linejoin="round"`, and ends stopping at a clearance are cut, not
capped (see *Cut ends, not caps*).

### Corner Radius

Corner radii describe the **visible outer edge** of the painted stroke, so path
`rx = visible radius − stroke-width / 2` (already applied in the table). Use the
**large** radius on primary outer frames/containers (`≥ 10px` at `16×16`,
`≥ 12px` at `20×20`, or full keyline shapes) and the **small** radius on compact
or inner shapes. At `16×16`, an intermediate `1.5px` visible radius (`rx="1"`)
is also valid when matching an icon family (e.g., `studio/add-component.svg`,
`studio/layout-inspector.svg`).

### Keyline Dimensions & Inner Strokes

Fit primary shapes to these optical keylines (review overlays only, never
exported geometry). Overlaid modifiers may extend into the `1px` outer padding
as long as painted bounds stay inside the canvas. At `14×14`, formal keylines do
not apply: target a `12×12`–`14×14` live area (`1px` padding default; `0px`
allowed when a form or modifier needs the full `14×14` canvas).

| Shape | `20×20` (`18×18` live area) | `16×16` (`14×14` live area) |
| :--- | :--- | :--- |
| **Circle** | `18×18px` | `14×14px` |
| **Square** | `16×16px` | `12×12px` |
| **Vertical rectangle** | `14×18px` | `10×14px` |
| **Horizontal rectangle** | `18×14px` | `14×10px` |

To place a stroked shape's outer edge cleanly on a keyline, inset the path by
the table's **Inner-stroke inset** on each side:
- **`20×20`**: `18×18` circle at `(10, 10)` → `r="8.25"`; `16×16` square at
  `2..18` → `x="2.75" y="2.75" width="14.5" height="14.5" rx="1.25"`.
- **`16×16`**: `14×14` circle at `(8, 8)` → `r="6.5"`; `12×12` square at `2..14`
  → `x="2.5" y="2.5" width="11" height="11" rx="1.5"`.

### Diagonals and Arrows

- **Angles**: Draw strokes at 0°, 45°, or 90°. Avoid arbitrary angles.
  Established symbols keep their canonical angles (e.g., play or warning
  triangles, bug legs in `intellij/debug.svg`); snap vertices to the `0.5px`
  grid and cite the precedent icon in the Deviation Report.
- **Diagonal stroke weight**: Keep the same `stroke-width` on diagonals as on
  straight strokes — do not thicken them to compensate for 1× anti-aliasing.
- **Arrowheads**: Arms meet the shaft at 45° (90° apart) with a round join at
  the tip — never a sharp miter. Horizontal/vertical shafts have diagonal arms;
  diagonal shafts have horizontal and vertical arms.

### Connected Shapes, Cutouts, and Modifiers

- **Connected parts of one glyph**: Form a continuous visual union without
  artificial clearance gaps. Overlapping opaque strokes are sufficient; flatten
  to a Boolean union only to remove internal seams, preserving intentional holes.
- **Concentric shapes**: Nested or parallel curves must share a center (e.g.,
  an arc `2px` outside `r="6.5"` uses `r="8.5"` around the same center) so the
  gap stays uniform. Treat off-grid arc endpoints on that circle as derived
  points (Section 1).
- **Distinct overlapping objects**: Interrupt rear strokes only where needed for
  legibility — do not cut merely because two elements intersect or change color.
- **Modifier placement & sizing**: A modifier is a small established symbol
  overlaid on a dominant base. Bottom-right is the default; use another corner
  or a centered edge on a symmetric base (e.g., `studio/add-component.svg`) when
  that preserves the base silhouette. Author at the target size from the table
  (never shrink a full-size icon) and never nest a sub-modifier inside a
  modifier.
- **Modifier clearance**: Leave the table's clearance between painted edges of
  modifier and base, cutting rear geometry so the gap stays transparent. Follow
  the modifier's outer silhouette wherever it approaches or overlaps the base
  (including protrusions such as a magnifier handle if they face the base); a
  simpler circle or box contour is fine when only that side meets the base.
- **Slashes and occluding marks**: Cut underlying strokes around the crossing so
  the mark reads cleanly, leaving at least the table's modifier clearance
  (one-sided clearance is valid when matching the icon family, as in
  `studio/show-constraints.svg`).
- **Cut ends, not caps**: Where a stroke stops at a clearance around a modifier,
  slash, or overlapping object, end it with a flat cut along the clearance
  contour rather than a round cap (which reads as a free end and eats half a
  stroke width into the gap). Implement this with a `<clipPath>` containing a
  `clip-rule="evenodd"` compound path (outer canvas rect minus the clearance
  hole) so strokes inside can keep round caps for their free ends.
  **Exception**: a stroke interrupted head-on along its own axis by a modifier
  with round ends (such as the plus in `studio/add-component.svg`) may end in
  round caps so both sides of the gap match.
- **Modifier color**: Keep the modifier's established semantic role (Section 3)
  and distinct silhouette — modifiers are not automatically blue.

## 3. Color Palette & Theme Variants

- **Attributes & exact hex only**: Set colors strictly via `fill="…"` and
  `stroke="…"` attributes (never `style`, `class`, or `<style>` CSS), using exact
  six-digit hex values from the tables below (`#FFFFFF`, never `#fff` or
  `white`; normalize `white` to `#FFFFFF` when authoring or fixing). Never
  invent hex values or mix legacy Classic UI colors (`#6E6E6E`, `#AFB1B3`,
  `#DB5860`, `#59A869`, `#389FD6`) — IntelliJ runtime recoloring matches exact
  attribute values.
- **Dark variants**: Map every element to the dark value in the same row/cell as
  its light value. When a light hex appears in multiple roles (e.g., `#818594`
  or `#FFFFFF`), pick the dark value for the element's role.
- **Theme parity**: Light and dark files must paint identical geometry; only
  colors differ. Authored pairs should keep identical SVG structure (differing
  non-painting wrappers or canvas clips are tolerated only when auditing shipped
  files).

### Neutral Colors

| Role | Light | Dark | Usage |
| :--- | :--- | :--- | :--- |
| **Default stroke** | `#6C707E` | `#CED0D6` | Primary neutral outline/stroke |
| **Default fill** | `#EBECF0` | `#43454A` | Soft neutral fill inside outlined shapes |
| **Muted stroke** | `#818594` | `#B4B8BF` | De-emphasized or recessed strokes |
| **Secondary stroke** | `#818594` | `#868A91` | Secondary detail lines or supporting geometry |
| **Monochrome** | `#000000` | `#FFFFFF` | High-contrast monochrome glyphs (e.g., badges/overlays) |
| **On solid** | `#FFFFFF` | `#FFFFFF` | Inner glyph on a non-yellow Solid fill |
| **On yellow solid** | `#FFFFFF` | `#5E4D33` | Inner glyph on a yellow Solid fill |

### Semantic Hue Colors

Each cell is `light` / `dark`.

| Hue | Stroke | Accent | Solid | Tint |
| :--- | :--- | :--- | :--- | :--- |
| **Blue** | `#3574F0` / `#548AF7` | `#3574F0` / `#548AF7` | `#3574F0` / `#548AF7` | `#EDF3FF` / `#25324D` |
| **Green** | `#208A3C` / `#57965C` | `#369650` / `#57965C` | `#55A76A` / `#57965C` | `#F2FCF3` / `#253627` |
| **Yellow** | `#C27D04` / `#D6AE58` | `#FFAF0F` / `#F2C55C` | `#FFAF0F` / `#F2C55C` | `#FFFAEB` / `#3D3223` |
| **Orange** | `#E66D17` / `#C77D55` | `#E66D17` / `#C77D55` | `#E66D17` / `#C77D55` | `#FFF4EB` / `#45322B` |
| **Red** | `#DB3B4B` / `#DB5C5C` | `#DB3B4B` / `#DB5C5C` | `#E55765` / `#DB5C5C` | `#FFF7F7` / `#402929` |
| **Purple** | `#834DF0` / `#A571E6` | `#834DF0` / `#A571E6` | `#834DF0` / `#A571E6` | `#FAF5FF` / `#2F2936` |

### Choosing the Right Role

- **Neutral**: Use **Default stroke**, optionally paired with **Default fill**
  for enclosed interiors; use **Muted** or **Secondary** for recessed or
  supporting lines, and **Monochrome** only for high-contrast glyphs.
- **Semantic outline**: Pair the hue's **Stroke** with its **Tint** for two-tone
  nodes, file types, or badges (outlined letterforms inside a tinted node also
  use the hue's **Stroke** as their fill, as in `intellij/interface.svg`). Use
  the hue's **Accent** for standalone colored strokes or modifiers on a neutral
  icon.
- **Semantic solid**: Use the hue's **Solid** for filled badges or status dots,
  with **On solid** (or **On yellow solid** for yellow) for inner glyphs.

## 4. SVG Audit & Fix Checklist

Check (and, when fixing, repair) in this order. Every check includes the
exceptions defined in the referenced section.

1. **Canvas, `viewBox` & filename**: Exact bounds (Section 1) and target
   icon-set filename convention (Section 2 *Filenames*).
2. **Padding & keylines**: Painted geometry stays inside the live area (outside
   the Section 2 outer padding, except overlaid modifiers) and aligns to Section
   2 keylines (N/A at `14×14`).
3. **Strokes, caps, joins, radii & angles**: `stroke-width`, caps/joins,
   inner-stroke inset, corner radii, diagonals, and arrowheads match Section 2.
4. **Connections, cutouts & modifiers**: Continuous unions, concentric curves,
   clearances, cut ends, placement, sizing, and semantic color match Section 2
   *Connected Shapes, Cutouts, and Modifiers*.
5. **Grid, live strokes & path hygiene**: Live strokes (or *Auditing Outlined
   Files* below), `0.5px` step, pixel-aligned centerlines, `≥ 1px` (`1.5px` at
   `20×20`) gaps, clean anchors/DOM, unique IDs, no masks/effects/`<text>`
   (Section 1).
6. **Colors & theme parity**: Attribute-only exact six-digit hex values, role
   mapping, and light/dark parity match Section 3.
7. **Render & inspect**: Rasterize with `rsvg-convert`, `resvg`, or a headless
   browser at 1×, 2×, and an 8×–16× nearest-neighbor zoom on light
   (`#FFFFFF`/`#F7F8FA`) and dark (`#1E1F22`/`#2B2D30`) backgrounds. Confirm
   joins connect, clearances follow the foreground silhouette, strokes read
   crisply, and both base and modifier are recognizable. If no rasterizer or
   image-inspection tool is available, do not guess or claim pass — log item 7
   as **Not checked (no rasterizer)** in the Deviation Report.

### Auditing Outlined Files

Many shipped icons export strokes as outlined filled paths whose caps/joins
become decimal Bezier curves. Audit them by **painted edges**:
- **Grid**: Straight edges of `1px` strokes land on whole pixels; `1.5px`
  strokes on `.25`/`.75` centerlines land on whole/half pixels. Curve control
  points are exempt from the `0.5px` step.
- **Stroke width, caps & joins**: Parallel edge spacing equals Section 2
  `stroke-width`; open ends and corners form semicircular caps / rounded joins.
- **Audit vs. fix**: In an audit-only review, report outlined linework as a
  deviation rather than redrawing. When fixing or editing geometry, redraw as
  live strokes and compare 1×/2× rasters against the original (item 7).

### Deviation Report

End every authoring, audit, or fix task with a per-icon report containing:
- **Deviations**: every unmet rule (and any unchecked item, including item 7)
  with the reason, or `None`.
- **Exceptions used**: any sanctioned exception applied (derived points with
  construction, canonical angles with precedent icon, font fallback, etc.), or
  `None`.

Do not claim any checklist item passed unless you actually verified it.

## 5. Converting From Other Icon Sets

When redrawing an icon from another set (e.g., a 24px Material Symbol), do not
scale the source down; re-author it at the target size.

- **Count what fits**: At `16×16`, a `1px` stroke plus a `1px` gap is a `2px`
  pitch, so a `14px` live area holds at most seven parallel strokes — and
  concentric features (rings, fingerprint ridges) cross the live area twice,
  leaving room for at most three rings around a center (e.g., six fingerprint
  ridges become four). Drop repeated features rather than compressing gaps below
  the Section 1 minimum.
- **Keep the identifying features**: Preserve the silhouette and the one or two
  details that identify the symbol; simplify everything else.
- **Convert fills to outlines**: Turn filled glyphs into live strokes, keeping
  fills only for the filled-by-design roles in Section 1.
- **Compare against the source**: Render the redraw at 1× next to the source at
  its native size (item 7) and verify the symbol reads the same.
