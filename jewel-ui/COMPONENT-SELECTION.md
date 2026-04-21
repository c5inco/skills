# Component Selection

Pick the component that matches the user's intent, not just the first one that works. When multiple Jewel components could solve a problem, these rules align with the JetBrains IntelliJ Platform UI Guidelines — the authority for IntelliJ-styled UX. Jewel's API follows those guidelines.

## How to Use This File

1. Identify the interaction shape: mutually exclusive pick, multi-select, pick-or-type, binary toggle, action row, etc.
2. Apply the rule below.
3. Cross-check the external JetBrains guideline linked at the end of the section when behavior is non-obvious.

## Mutually Exclusive Selection (pick exactly one)

| Shape | Use |
|---|---|
| 2–4 options, short labels | `RadioButtonRow` group under a `GroupHeader` |
| 2–4 options, very short labels, emphasizing toggle semantics | `SegmentedControl` / `SegmentedControlButton` |
| 5+ options, long labels, limited space, or less-frequent setting | `ListComboBox` / `ComboBox` |
| User may enter a custom value in addition to picking | `EditableComboBox` |

Do **not** build a row of 3 `DefaultButton`s (or `OutlinedButton`s) as an exclusive selector — that's an action row, not a selection control.

Source: [Radio Button](https://plugins.jetbrains.com/docs/intellij/radio-button.html), [Combo Box](https://plugins.jetbrains.com/docs/intellij/combo-box.html).

## Multi-Select and Toggles

| Shape | Use |
|---|---|
| Independent boolean items | Group of `CheckboxRow` in a `Column` |
| Items share a "select all" parent | `ThreeStateCheckbox` as parent + `CheckboxRow` children |
| Binary yes/no with a clear default state | Single `Checkbox` / `CheckboxRow` |
| Binary yes/no where the "off" state is unclear from the label | Two `RadioButton`s with explicit labels for both states |

Source: [Checkbox](https://plugins.jetbrains.com/docs/intellij/checkbox.html).

## Pick-or-Type

| Shape | Use |
|---|---|
| Predefined values, no custom input allowed | `ListComboBox` / `Dropdown` |
| Predefined values + allow custom input | `EditableComboBox` |
| Very large list; user already knows the value | `TextField` with completion (not a combo box) |
| No initial values available | `TextField` — never show an empty combo box |

Source: [Combo Box](https://plugins.jetbrains.com/docs/intellij/combo-box.html).

## Action Buttons

| Shape | Use |
|---|---|
| Primary action in a form, dialog, or confirmation | `DefaultButton` |
| Secondary / cancel / alternative action | `OutlinedButton` |
| Row of primary actions (rare) | One `DefaultButton` + `OutlinedButton`s; never two `DefaultButton`s |
| Icon-only action | `IconButton` / `IconActionButton` |

The primary action must be visually distinct. Destructive actions (delete, discard, remove) are still the primary button of the dialog — paired with an outlined "Cancel" — but should use clear, imperative labels (`"Delete"`, not `"Yes"`) so users don't confirm by reflex.

## Writing Component Labels (Shared Rules)

1. **Sentence-style capitalization for most controls** (checkboxes, radios, links, group headers, tooltips, helper text). **Exception: `DefaultButton` / `OutlinedButton` / `DefaultSplitButton` / `OutlinedSplitButton` use title case** — `"Save Changes"`, not `"Save changes"`. The button case exception is an IntelliJ/Jewel convention; do not default to sentence case for buttons.
2. No ending punctuation, **except** group labels (radio / checkbox group headers), which end with `:`.
3. Imperative verb form.
4. Avoid negation. Exception: `"Do not show again"`.
5. Keep labels short; wrap to at most two lines.
6. Checkbox label always on the right of the box; in tables, put it in the column header — don't repeat on every row.
7. **Button labels never include `"Now"`** — `"Apply"`, not `"Apply Now"`; `"Save"`, not `"Save Now"`. A button is implicitly immediate; `"Now"` adds no information.
8. **Placeholders are not labels.** Never rely on a `TextField` placeholder to carry the field's purpose — placeholders hide as the user types. Always pair a field with a visible label above or to the left; use the placeholder for example input only (`"name@example.com"`, not `"Email address"`).
9. **Link text must be descriptive.** Do **not** use `"click here"`, `"learn more"`, `"navigate"`, or similar bare phrasings as `Link` text. The link itself implies action; the text should name the destination (`"Open documentation"`, `"View the migration guide"`).
10. **External-link icon**: append a trailing arrow (↗) or external-link icon exclusively on `Link`s that leave the app. Internal navigation links within the same window get no icon.

Source: [Radio Button](https://plugins.jetbrains.com/docs/intellij/radio-button.html), [Checkbox](https://plugins.jetbrains.com/docs/intellij/checkbox.html), [Button](https://plugins.jetbrains.com/docs/intellij/button.html), [Input Field](https://plugins.jetbrains.com/docs/intellij/input-field.html), [Link](https://plugins.jetbrains.com/docs/intellij/link.html).

## Canonical Source Links

Authority: JetBrains IntelliJ Platform UI Guidelines. The Jewel API implements these components; the guidelines define the UX contract.

- [Components index](https://plugins.jetbrains.com/docs/intellij/components.html)
- [Principles](https://plugins.jetbrains.com/docs/intellij/principles.html) — layout, typography, validation errors, platform theme colors
- [Radio Button](https://plugins.jetbrains.com/docs/intellij/radio-button.html)
- [Checkbox](https://plugins.jetbrains.com/docs/intellij/checkbox.html)
- [Combo Box](https://plugins.jetbrains.com/docs/intellij/combo-box.html)
- [Button](https://plugins.jetbrains.com/docs/intellij/button.html)
- [Group Header](https://plugins.jetbrains.com/docs/intellij/group-header.html)
- [Writing Short and Clear](https://plugins.jetbrains.com/docs/intellij/writing-short.html)
- [Capitalization](https://plugins.jetbrains.com/docs/intellij/capitalization.html)
