---
id: 12-confirm-delete-dialog
category: howto
difficulty: easy
---

## Prompt

> I need a dialog to confirm the user wants to delete an item. Show me the buttons.

## Expected skill behavior

1. Routes to COMPONENT-SELECTION.md "Action Buttons" rule.
2. Uses one primary and one secondary button — not two of the same variant.
3. The primary (destructive) action uses `DefaultButton`; the cancel uses `OutlinedButton`.
4. Action labels are imperative and explicit ("Delete", not "Yes" or "OK").

## Pass criteria

- [ ] Uses `DefaultButton` for the destructive action (Delete).
- [ ] Uses `OutlinedButton` for the secondary / cancel action.
- [ ] Does **not** use two `DefaultButton`s or two `OutlinedButton`s side by side.
- [ ] Primary action label is imperative and explicit (e.g. "Delete", "Remove") — not "Yes", "OK", or "Confirm" alone.
- [ ] Cancel / dismiss path is clearly the secondary action (visually less prominent, labeled as "Cancel" or equivalent).

## Notes

The IntelliJ Platform doesn't currently have a published "Dangerous Actions" principle page (it's a placeholder in the TOC), so the primary/secondary button rule comes from the general [Button guidance](https://plugins.jetbrains.com/docs/intellij/button.html) plus Jewel convention.
