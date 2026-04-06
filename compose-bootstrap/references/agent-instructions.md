# Agent Instructions Template (`AGENTS.md` by default)

This reference contains a provider-agnostic template for the main agent instructions file.
When generating, replace placeholders (`{{...}}`) with values from the Phase 1 analysis.

## Filename selection

Choose the filename using these rules:

1. If an agent-instruction file already exists (`AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, etc.),
   update the existing file.
2. If none exists, generate `AGENTS.md` at the project root.
3. If the user asks for a specific filename, follow that preference.

## Template

```markdown
# {{INSTRUCTION_FILENAME}}

## Project Overview

{{PROJECT_DESCRIPTION — ask the user for a one-liner, or infer from README/build config}}

## Build & Run

{{Adapt these commands based on the detected project type and build setup}}

\`\`\`bash
./gradlew build       # compile all modules
./gradlew test        # run unit tests
./gradlew check       # detekt + ktfmt + tests — run before every push
\`\`\`

{{If Android, add:}}
\`\`\`bash
./gradlew connectedCheck   # instrumented tests (requires device/emulator)
\`\`\`

{{If Desktop with compose-driver, add:}}
\`\`\`bash
./gradlew test -PincludeTags=compose-driver   # UI automation tests
\`\`\`

## Non-Negotiables

### TDD First

Write the failing test before the implementation. Then make it pass with the minimum change.

1. Write the test.
2. Run the targeted test.
3. Prove it fails (red) before editing production code.
4. Implement the minimum fix.
5. Re-run tests to green.

### Detekt and Suppressions

- Never edit `detekt.yml` or custom detekt rules without explicit permission.
- Do not create or update detekt baselines.
- Avoid `@Suppress` annotations — fix findings at the source.
- If a finding cannot be fixed, surface it and wait for instructions.

### Regressions and Scope

- Changes must relate to the current task. Unrelated changes are forbidden.
- Any behavioral change not requested by the user is a regression — flag it.
- Refactors cannot change behavior. Keep cleanup separate from feature work.
- Changes must never result in broken features unless explicitly agreed upon with the user
  as part of a phased implementation plan.

## Working Style

**Minimize interruptions.** Scan the code before forming questions — most ambiguities resolve
on their own. If something is genuinely blocking, ask all questions at once before starting
work. Mid-task, prefer a safe assumption over interrupting.

**Be explicit about working directory changes.** Start from the project root by default. If
you need a different directory, use an explicit `cd /absolute/path` first.

## PR Rules

Do not open or push to a PR until:
1. `./gradlew check` passes locally.
2. CI is green on the PR branch.
3. TDD cycle is complete — every new test was red before its implementation.

## Source of Truth Docs

| Document | Purpose |
|----------|---------|
| [docs/CONVENTIONS.md](docs/CONVENTIONS.md) | Code style, file placement, git workflow |
| [docs/TESTING.md](docs/TESTING.md) | TDD flow, test conventions |
| [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) | Module map, dependency direction |
```

## Customization guidance

When generating this file, apply these rules:

1. **Build commands**: Use the actual tasks available in the project. If there's a custom
   `run` task, include it. If the project uses `assemble` instead of `build`, adjust.

2. **Project overview**: If a README exists, extract a summary. Otherwise ask the user or
   leave a `TODO:` placeholder.

3. **Module-specific commands**: For multi-module projects, include module-prefixed commands
   (e.g., `./gradlew :app:test`, `./gradlew :core:check`).

4. **Worktree policy**: Include this section if the project uses git worktrees or the user
   requests it. Otherwise omit — it adds complexity for teams that don't use worktrees.

   ```markdown
   ### Worktree Policy

   Before writing any non-gitignored file, check if you are already in a worktree or on a
   non-main branch. If neither, ask the user if they'd like a worktree for isolation.
   ```

5. **Additional non-negotiables**: If the project has domain-specific invariants (e.g.,
   "never call the API without authentication", "all database access goes through the
   repository layer"), add them as additional non-negotiables. These emerge from the
   codebase analysis — look for patterns in existing code and docs.
