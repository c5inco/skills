# Conventions Template (docs/CONVENTIONS.md)

This reference contains the template for the project conventions doc. Adapt based on the
Phase 1 analysis — especially the file placement table and UI work boundary.

## Template

```markdown
# Conventions

## Code Style (Detekt-Aligned)

These rules apply to all new or modified code, including agent-generated code.

- **No wildcard imports** — always use explicit imports.
- **Line length <= 120 characters** — split long chains and log statements.
- **No magic numbers** — extract named constants or theme tokens.
- **Exception handling** — do not catch broad `Exception`/`Throwable` except at process
  boundaries. Never swallow exceptions silently; log context and return a typed failure.
- **Method focus** — keep methods focused; extract helpers when branching or looping
  accumulates.

{{If Compose project, include:}}
## Composable Conventions

- For reusable composables, accept `modifier: Modifier = Modifier` as the first parameter.
- Treat Compose UI as a render layer, not a work layer.
- Allowed in composables: ephemeral UI-local state (`remember` for scroll/animation/
  expanded flags, local focus state, transient interaction state).
- Not allowed in composables: direct file/DB/network/process I/O, business computations.
- UI events should call presenter/ViewModel APIs; they return/update view state that UI
  renders.

## File Placement

{{Generate this table based on the detected module structure. Below is a starting point
  — adjust package paths and descriptions to match the actual project.}}

| What | Where |
|------|-------|
| Data models | `core/model/` or `data/model/` |
| Repository interfaces | `core/data/` or `domain/` |
| Repository implementations | `data/` |
| ViewModels / Presenters | `feature/<name>/` or `ui/<name>/` |
| Reusable UI components | `ui/components/` or `core/ui/` |
| Screen composables | `feature/<name>/` or `ui/screens/` |
| Navigation | `navigation/` or `app/` |

## Git Workflow

- Do not push directly to `main` without confirmation.
- Always run `./gradlew check` before pushing or opening a PR.
- Use descriptive branch names: `fix/issue-number-description`, `feat/feature-name`.
- Commit messages should explain what changed and why, not just restate file names.
- Reference issue numbers in PR descriptions: "Fixes #27".
```

## Customization guidance

1. **File placement**: This is the most project-specific section. If the analysis finds an
   established package structure, mirror it in the table. If the project is new, use
   conventional patterns for the detected project type:
   - **Android (multi-module)**: `:app`, `:core:data`, `:core:model`, `:core:ui`,
     `:feature:*`
   - **Android (single-module)**: `data/`, `domain/`, `ui/`, `model/`
   - **Desktop**: `state/`, `ui/`, `rpc/` or `data/`
   - **KMP**: `commonMain/`, `androidMain/`, `desktopMain/`, etc.

2. **Composable conventions**: Include for any Compose project. The UI work boundary is
   important for agents — without it, they tend to put business logic in composables.

3. **Additional conventions**: Look for patterns in the existing codebase:
   - Dependency injection approach (Hilt, Koin, manual)
   - Networking patterns (Retrofit, Ktor)
   - State management (ViewModel, MVI, unidirectional data flow)
   Add these as sections if they represent established patterns.
