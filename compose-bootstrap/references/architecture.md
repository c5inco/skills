# Architecture Template (docs/ARCHITECTURE.md)

This reference contains the skeleton for the architecture doc. The skill generates this as
a starting point — the user fills it in as the project evolves.

If the Phase 1 analysis detects an existing module structure, pre-fill the module map section.
Otherwise leave it as a template with example entries.

## Template

```markdown
# Architecture

## Module Map

{{For multi-module projects, list each module with its purpose:}}

| Module | Purpose | Dependencies |
|--------|---------|-------------|
| `:app` | Application entry point, navigation | `:core:ui`, `:feature:*` |
| `:core:model` | Domain models, shared types | None |
| `:core:data` | Repository interfaces, data sources | `:core:model` |
| `:core:ui` | Shared composables, theme, design tokens | `:core:model` |
| `:feature:home` | Home screen feature | `:core:ui`, `:core:data` |

{{For single-module projects, list packages instead:}}

| Package | Purpose |
|---------|---------|
| `model/` | Domain models and data classes |
| `data/` | Repositories, data sources, networking |
| `ui/` | Composables, screens, components |
| `ui/theme/` | Theme, colors, typography |

## Dependency Direction

Dependencies flow inward: UI -> Domain -> Data (or as appropriate for the project).

- **UI layer** depends on domain/state layer
- **Domain/state layer** has no UI dependencies
- **Data layer** implements domain interfaces

{{Adjust for the actual architecture pattern detected — MVI, MVVM, Clean Architecture, etc.}}

## Key Patterns

Document recurring patterns used in the codebase:

- **State management**: {{ViewModel + StateFlow, MVI with reducers, etc.}}
- **Navigation**: {{Compose Navigation, custom router, etc.}}
- **Dependency injection**: {{Hilt, Koin, manual, etc.}}
- **Async work**: {{Coroutines + Flow, etc.}}

## Architectural Invariants

Rules that must not be violated:

1. {{e.g., "UI composables never access the database directly"}}
2. {{e.g., "All network calls go through the repository layer"}}
3. {{e.g., "Feature modules do not depend on each other"}}
```

## Customization guidance

1. **Pre-fill what you can detect**: Module names, package structure, and dependency
   declarations are all visible in build files and source trees.

2. **Don't invent patterns**: If the codebase doesn't clearly follow a pattern, leave
   the "Key Patterns" section as a template. Documenting a pattern that doesn't exist
   is worse than having no documentation.

3. **Invariants**: These are the most valuable part of the architecture doc for agents.
   Look for enforcement in the build (module dependencies, lint rules) or in existing
   docs. If none exist, leave as a template — the user should define these.
