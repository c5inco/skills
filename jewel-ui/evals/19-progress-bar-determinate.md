---
id: 19-progress-bar-determinate
category: howto
difficulty: medium
---

## Prompt

> I'm compiling the user's project. Show me a progress indicator.

## Expected skill behavior

1. Distinguishes determinate vs indeterminate: compilation has a known number of files / steps, so `HorizontalProgressBar` with a computed fraction is the right shape. If steps aren't enumerable, `IndeterminateHorizontalProgressBar` is the fallback.
2. Runs in the background, not a modal blocking dialog — the user should be able to keep working.
3. Uses "Cancel" for safely interruptible processes, "Stop" for irreversible ones — compilation is typically "Cancel".
4. Avoids offering a pause option (the IntelliJ guideline explicitly deprecates pause in favor of background execution).
5. Does not keep the progress indicator visible post-completion.

## Pass criteria

- [ ] Recommends `HorizontalProgressBar` (determinate) or `IndeterminateHorizontalProgressBar` with an explicit note that determinate is preferred when duration is known.
- [ ] Mentions running the operation in the background (or in a non-blocking surface), not a modal dialog.
- [ ] Includes a Cancel action (not a Pause action); or explicitly notes that pause should be avoided.
- [ ] Mentions dismissing the indicator on completion, or at least does not suggest leaving it visible.

## Notes

The guideline's anti-pause rule is specific to IntelliJ and not broadly known — a probing signal. The `HorizontalProgressBar` determinate-when-possible rule is standard UX but worth codifying.

Source: [Progress Bar guideline](https://plugins.jetbrains.com/docs/intellij/progress-bar.html).
