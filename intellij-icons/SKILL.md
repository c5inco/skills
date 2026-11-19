---
name: intellij-icons
description: Creates, audits, and fixes SVG icons in the IntelliJ icon style. Use when asked to review, fix, optimize, rename, or author SVGs following IntelliJ icon guidelines (20x20, 16x16, and 14x14 grids, outline style, stroke weights, corner radii, path hygiene, naming, and light/dark color variants).
---

# Icon Guidelines

Use these rules when creating, auditing, or fixing SVG icons in the **IntelliJ** style.
Section 2 is the single source of truth for per-size values; other sections
refer to it rather than repeating them.

## 1. General Rules

- **Outline first**: Use outline icons whenever possible rather than filled
  silhouettes.
- **Flat style**: Keep icons strictly flat — no gradients, drop shadows, blur
  filters, or 3D effects.
- **Minimal detail**: Use the minimum amount of geometry needed to clearly
  convey meaning.
- **0.5px minimal step**: Snap coordinates, dimensions, and offsets to `0.5px`
  increments. Avoid noisy sub-pixel decimals (e.g., `3.00012` → `3`, `4.4998` →
  `4.5`). **Exception**: values derived from half the stroke width are correct
  as-is and must not be re-snapped — e.g., the `0.75px` inner-stroke inset at
  `20×20` (`r="8.25"`, `x="2.75"`) and the path `rx` values in Section 2
  (`1.25`, `0.25`).
- **No excessive anchor points**: Simplify `<path>` geometry to remove redundant
  vertices, collinear points, and unnecessary curve segments.
- **Letterforms**: Use **JetBrains Sans** whenever an icon includes a letterform
  (e.g., Class, Interface, etc.), and convert the text to outlined paths. Never
  ship a `<text>` element.
- **Exact canvas bounds**: Set `width`, `height`, and `viewBox` to the exact
  icon size (e.g., `0 0 16 16`) and ensure all visible geometry stays within
  bounds (a `<clipPath>` to the canvas bounds is fine if necessary).
- **Avoid masks**: Create cutouts, clearances, and gaps by cutting the actual
  path geometry or with a `<clipPath>`. Use `<mask>` only as a last resort when
  neither is feasible.
- **Colors via attributes only**: Set colors with `fill="…"` and `stroke="…"`
  attributes. Do not use `style="…"`, `class`, or `<style>` CSS — IntelliJ's
  runtime recoloring matches on the attribute values.

## 2. Size Specifications

Match the SVG canvas size to the UI surface where the icon is used.

| Property | `20×20` | `16×16` | `14×14` |
| :--- | :--- | :--- | :--- |
| **Usage** | Main toolbar, Tool windows | Default for most UI elements (Toolbars, Trees, Menus, etc.) | Gutter, Status bar |
| **Filename (light / dark)** | `name@20x20.svg` / `name@20x20_dark.svg` | `name.svg` / `name_dark.svg` | `name@14x14.svg` / `name@14x14_dark.svg` |
| **`stroke-width`** | `1.5` | `1` | `1` |
| **End caps** | Round (`stroke-linecap="round"`) | Round allowed | — |
| **Outer padding** (canvas edge to painted geometry) | `1px` | `1px` | `0–1px` |
| **Inner-stroke inset** (larger forms) | `0.75px` | `0.5px` | — |
| **Corner radius, large shapes** (visible outer edge) | `2px` → path `rx="1.25"` | `2px` → path `rx="1.5"` | `1px` → path `rx="0.5"` |
| **Corner radius, small shapes** (visible outer edge) | `1px` → path `rx="0.25"` | `1px` → path `rx="0.5"` | `1px` → path `rx="0.5"` |
| **Stroke continuity** | Continuous unless broken segments improve legibility | Join connected parts (see below) | Join connected parts (see below) |
| **Modifier visual size** | ~`7.5–11px` | ~`6–9px` | ~`6–9px` |
| **Modifier `stroke-width`** | `1.5` | `1` | `1` |
| **Modifier clearance** | ≥ `1.5px`, typically `1.5–2.5px` | ≥ `1px`, typically `1–2px` | ≥ `1px`, typically `1–2px` |

### Corner Radius

Corner radii always describe the **visible outer edge** of the painted stroke.
Because SVG strokes are centered on the path, the path's `rx` is the visible
radius minus half the stroke width: `rx = radius − stroke-width / 2`. The `rx`
values in the table above already apply this.

### Keyline Dimensions (`20×20` and `16×16`, `1px` outer padding on all sides)

Fit primary shapes to these optical keylines so icons maintain consistent visual
weight. Overlaid modifiers may use the padding area as described below.

| Shape | `20×20` (`18×18` live area) | `16×16` (`14×14` live area) |
| :--- | :--- | :--- |
| **Circle** | `18×18px` | `14×14px` |
| **Square** | `16×16px` | `12×12px` |
| **Vertical rectangle** | `14×18px` | `10×14px` |
| **Horizontal rectangle** | `18×14px` | `14×10px` |

### Simulating Inner Strokes

To achieve an **inner stroke** on larger forms so the outer visual edge sits
cleanly on the keyline (and does not bleed into the `1px` padding), inset the
path by the table's inset value on each edge:

- **`20×20`**: an `18×18` circle centered at `(10, 10)` uses `r="8.25"`; a
  `16×16` square from `x=2..18` uses `x="2.75" y="2.75" width="14.5" height="14.5" rx="1.25"`.
- **`16×16`**: a `14×14` circle centered at `(8, 8)` uses `r="6.5"`; a `12×12`
  square from `x=2..14` uses `x="2.5" y="2.5" width="11" height="11" rx="1.5"`.

### Connected Shapes, Cutouts, and Modifiers

- **Connected parts of one glyph**: Make their painted geometry a continuous visual union, without artificial clearance gaps. Overlapping opaque shapes are sufficient; flatten to a Boolean union only when needed to remove internal seams. Preserve intentional interior holes, such as the center of an outlined ring.
- **Distinct overlapping objects**: Interrupt the rear object's strokes when needed to keep the foreground object recognizable. Do not add cuts merely because two SVG elements intersect or use different colors.
- **Modifier hierarchy**: A modifier is a small symbol overlaid on a dominant base icon, not a connected structural part. Reuse an established modifier where possible. Bottom-right is the default; use another corner when that preserves the base silhouette or matches the relevant icon family.
- **Modifier size and detail**: Use the modifier size and stroke from the table, according to weight and catalog references. The `16×16` values are the reference spec; the `20×20` values scale them proportionally (×1.25), and `14×14` reuses them. Author at the target size with pixel-aligned geometry; do not proportionally shrink a full-size icon and its stroke. Do not add a sub-modifier inside a modifier. If its identity does not survive at this size, use a simpler established symbol or a standalone icon.
- **Modifier clearance**: Leave the clearance from the table between modifier and base. Follow the modifier's entire outer silhouette, including protrusions such as a magnifier handle; do not erase a generic bounding rectangle or only the lens. Cut the rear geometry so the clearance stays transparent on different backgrounds. A modifier may use the outer-padding area, but its painted bounds must stay inside the canvas.
- **Slashes and other occluding marks**: Cut the underlying strokes around the crossing so the mark remains legible; do not simply paint a slash over intact details. Follow an existing icon-family reference for its clearance.
- **Modifier color**: Preserve the established symbol's semantic palette role from Section 3; modifiers are not automatically blue. Retain shape differences so color is not the only way to distinguish concepts.

Catalog references: [connected zoom plus](https://intellij-icons.web.app/icons/AllIcons/expui/image/zoomIn.svg), [magnifier modifier](https://studio-icons.web.app/icons/shell/menu/layout-inspector.svg), [occluding slash](https://studio-icons.web.app/icons/layout-editor/toolbar/show-constraints.svg), and [stop modifier](https://intellij-icons.web.app/icons/AllIcons/expui/actions/restartStop.svg). The [general JetBrains modifier guide](https://plugins.jetbrains.com/docs/intellij/icons-style.html#modifier) supports corner placement, 6–9px sizing, and 1–2px spacing; its legacy stroke and color rules do not override this skill's values.

## 3. Color Palette & Theme Variants

Always use exact hex values from the IntelliJ UI palette below and maintain paired
light and dark SVG files. DO NOT invent ad-hoc hex values or mix in legacy
Classic UI colors (e.g., `#6E6E6E`, `#AFB1B3`, `#DB5860`, `#59A869`, `#389FD6`)
— IntelliJ Platform themes rely on exact hex matching for runtime recoloring.

**Dark variants**: For every element, use the dark value listed in the same row
(or cell) as its light value, literally. Some light values are shared by
several roles (e.g., `#818594` is both Muted stroke and Secondary stroke);
decide which role the element plays, then use that role's dark value.

### Neutral Colors

| Role | Light | Dark | Usage |
| :--- | :--- | :--- | :--- |
| **Default stroke** | `#6C707E` | `#CED0D6` | Primary neutral outline/stroke for standard UI icons |
| **Default fill** | `#EBECF0` | `#43454A` | Soft neutral fill inside outlined shapes |
| **Muted stroke** | `#818594` | `#B4B8BF` | De-emphasized or subtly recessed strokes |
| **Secondary stroke** | `#818594` | `#868A91` | Secondary detail lines or supporting geometry |
| **Monochrome** | `#000000` | `#FFFFFF` | High-contrast monochrome glyphs |
| **On solid** | `#FFFFFF` | `#FFFFFF` | Inner glyph drawn on top of a Solid fill |
| **On yellow solid** | `#FFFFFF` | `#5E4D33` | Inner glyph drawn on top of a yellow Solid fill |

### Semantic Hue Colors

Each cell is `light` / `dark`.

| Hue | Stroke | Accent | Solid | Tint |
| :--- | :--- | :--- | :--- | :--- |
| **Blue** | `#3574F0` / `#548AF7` | `#3574F0` / `#548AF7` | `#3574F0` / `#548AF7` | `#EDF3FF` / `#25324D` |
| **Green** | `#208A3C` / `#57965C` | `#369650` / `#57965C` | `#55A76A` / `#57965C` | `#F2FCF3` / `#253627` |
| **Yellow** | `#C27D04` / `#D6AE58` | `#FFAF0F` / `#F2C55C` | `#FFAF0F` / `#F2C55C` | `#FFFAEB` / `#3D3223` |
| **Orange** | `#E56D17` / `#C77D55` | `#E56D17` / `#C77D55` | `#E56D17` / `#C77D55` | `#FFF4EB` / `#45322B` |
| **Red** | `#DB3B4B` / `#DB5C5C` | `#DB3B4B` / `#DB5C5C` | `#E55765` / `#DB5C5C` | `#FFF7F7` / `#402929` |
| **Purple** | `#834DF0` / `#A571E6` | `#834DF0` / `#A571E6` | `#834DF0` / `#A571E6` | `#FAF5FF` / `#2F2936` |

### Choosing the Right Role

- **General (neutral)**: Use **Default stroke**, optionally backed by
  **Default fill** for enclosed forms.
- **Outline (semantic)**: Pair the hue's **Stroke** with its **Tint** for
  two-tone nodes, file types, or badges; use the hue's **Accent** for
  standalone colored strokes/modifiers on a neutral icon.
- **Solid (semantic)**: Use the hue's **Solid** for filled badges or status
  dots, with **On solid** (or **On yellow solid** for yellow) for inner glyphs.

## 4. SVG Audit & Fix Checklist

When auditing or fixing an SVG icon, check and repair in this order. All
per-size values come from the Section 2 table.

1. **Canvas, `viewBox` & filename**: `width`, `height`, and `viewBox` match
   the intended size, and the filename follows the Section 2 pattern.
2. **Padding & keylines**: Painted strokes stay inside the Section 2 outer padding
   and align to the keylines, except for overlaid modifiers.
3. **Stroke, caps & radii**: `stroke-width`, end caps, inner-stroke inset, and
   corner radii (visible outer edge → path `rx`) match the Section 2 table.
4. **Joins & modifiers**: Connected parts form a continuous union; distinct
   overlaps and slashes are cut where needed. Any modifier uses an established
   symbol, sits in a corner, matches the table's size, stroke, and clearance,
   has clearance that follows its full silhouette, and keeps its semantic color.
5. **Precision & path hygiene**: Snap to `0.5px` (respecting the stroke-derived
   exception), remove excessive anchor points, strip unused `<defs>`/`<g>`
   wrappers, remove gradients, shadows, and filters, replace masks with
   geometric cuts or clip paths where feasible, and convert any `<text>` to
   paths.
6. **Colors & theme parity**: Colors are set only via `fill`/`stroke`
   attributes (no `style`, `class`, or CSS); every hex is an exact Section 3
   value; both light and dark variants exist with identical geometry, and each
   dark color is the table's dark value for the same role.
7. **Render & inspect**: Inspect native-size 1× and 2× rasters and
   nearest-neighbor pixel enlargements on light and dark backgrounds. Check
   that intended joins remain connected, clearance follows the foreground
   silhouette, and both the base and any modifier are recognizable. Keylines
   are review overlays, not exported geometry.
