---
name: compose-bootstrap
description: >
  Bootstrap a Compose project with agentic-coding infrastructure: agent instructions,
  detekt config, ktfmt setup, CI pipeline, testing conventions, and compose-driver. Use this skill
  when the user wants to set up a new Compose project for AI-assisted development, add agentic
  infrastructure to an existing Compose codebase, or prepare a Compose Desktop / Jetpack Compose /
  Compose Multiplatform project for effective agent collaboration. Also trigger when the user says
  things like "set up this project for AI coding", "add code quality tooling", "bootstrap for
  agentic coding", or "make this repo agent-ready".
---

# Compose Bootstrap

Set up a Compose project with the infrastructure that makes agentic coding productive: agent
instructions, code quality enforcement, CI, testing conventions, and UI test automation.

This skill does not generate Gradle projects from scratch — that's the IDE's job. Instead it
layers agentic infrastructure onto an existing (or freshly created) project. The skill analyzes
the codebase first, then proposes and generates only what's missing.

## Workflow

### Phase 1: Analyze the codebase

Before generating anything, scan the project to understand what exists. Run these checks and
record the results — they drive every decision in Phase 2.

#### 1a. Project type detection

Read `build.gradle.kts` (or `build.gradle`) at the root and in submodules. Identify:

- **Compose flavor**: Desktop (`org.jetbrains.compose`), Jetpack/Android
  (`com.android.application` or `com.android.library` + `androidx.compose`), or Multiplatform
  (`kotlin("multiplatform")` + compose targets). Multiple flavors may coexist in a multi-module
  project.
- **Compose targets**: Which platforms are configured — `jvm` (Desktop), `android`, `ios`,
  `wasmJs`, `js`. This matters for compose-driver setup (supports Desktop and Android).
- **Module structure**: Single-module or multi-module (check `settings.gradle.kts` for `include`
  statements).

#### 1b. Build tooling inventory

Check what's already configured:

| Check | How |
|-------|-----|
| Version catalog | `gradle/libs.versions.toml` exists? |
| Detekt plugin | `detekt` in plugins block or `buildscript` |
| Detekt config | `detekt.yml` or `detekt.yaml` at root |
| ktfmt plugin | `ktfmt` in plugins block |
| Compose rules | `compose-rules-detekt` or `io.nlopez.compose.rules` in dependencies |
| Compose-driver | `io.github.jdemeulenaere.compose.driver` in settings or build |
| Java/JDK version | `jvmToolchain` or `sourceCompatibility` |

#### 1c. Agent instructions inventory

Check for existing agent instruction files:

- `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.cursorrules`, `.github/copilot-instructions.md`
- `docs/` directory — any existing conventions, architecture, or testing docs
- `.agents/skills/` — existing skill infrastructure

#### 1d. CI inventory

- `.github/workflows/` — any existing GitHub Actions
- Other CI configs (`.circleci/`, `Jenkinsfile`, `.gitlab-ci.yml`, `bitbucket-pipelines.yml`)

#### 1e. Testing inventory

- Test framework in dependencies (JUnit 4, JUnit 5, AndroidX Test, Kotest)
- Test source directories (`src/test/`, `src/androidTest/`, etc.)
- Compose UI test dependencies (`compose.uiTest`, `ui-test-junit4`, etc.)
- Existing test tag infrastructure

### Phase 2: Propose changes

Present a summary to the user structured as:

```
## Codebase Analysis

**Project type**: [detected type]
**Modules**: [list]
**Compose targets**: [list]

## Already configured
- [x] Version catalog (gradle/libs.versions.toml)
- [x] JUnit 5
- ...

## Will add
1. detekt.yml — Compose-aware static analysis config
2. ktfmt plugin — Kotlin formatting (kotlinLangStyle)
3. AGENTS.md (or platform-specific equivalent) — Agent operating instructions
4. docs/CONVENTIONS.md — Code style and workflow conventions
5. docs/TESTING.md — TDD flow and test conventions
6. docs/ARCHITECTURE.md — Module map template
7. .github/workflows/ci.yml — CI pipeline
8. compose-driver — UI test automation

## Won't add (already exists)
- ...

Proceed?
```

Wait for confirmation before generating files. The user may want to remove items or adjust scope.

### Phase 3: Generate files

Generate each artifact, adapting to what Phase 1 detected. Read the appropriate reference file
for each artifact's template and customization rules.

#### Agent instructions — always generate or update

These are the core value of the skill. Read `references/agent-instructions.md` for the agent
instructions template and filename selection rules.

- If one agent instruction file already exists (`AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, etc.),
  update that file instead of creating duplicates.
- If none exists, generate `AGENTS.md` at the project root.
- If the user explicitly requests a provider-specific filename, follow their preference.

Customize the build commands and project-type-specific sections based on the Phase 1 analysis.

Read `references/conventions.md` for docs/CONVENTIONS.md. Adapt the file placement table and UI
work boundary section to the detected project structure.

Read `references/testing.md` for docs/TESTING.md. Select the right test framework examples based
on what Phase 1 found (JUnit 4 vs 5, Compose UI test variant).

Read `references/architecture.md` for the docs/ARCHITECTURE.md skeleton.

#### Detekt config — generate if not present

Read `assets/detekt.yml` for the Compose-aware configuration. This is a ready-to-use file
built on `buildUponDefaultConfig = true` with Compose-specific overrides.

If detekt is not in the build plugins yet, provide the user with a snippet to add it. Do not
modify build.gradle.kts directly — the build file structure varies too much across projects.
Instead, output the snippet and tell the user where to add it:

```
Add to your plugins block:
  alias(libs.plugins.detekt)  // or: id("dev.detekt") version "2.0.0-alpha.2"

Add to dependencies:
  detektPlugins("io.nlopez.compose.rules:detekt:<version>")

Add to your build.gradle.kts:
  detekt {
      buildUponDefaultConfig = true
      config.setFrom(files("detekt.yml"))
  }
```

Also provide version catalog entries if the project uses `libs.versions.toml`.

#### ktfmt — provide snippet if not present

Same approach: provide the plugin declaration and configuration snippet rather than editing
build files. The configuration is always `ktfmt { kotlinLangStyle() }`.

#### CI pipeline — generate if GitHub Actions and no check workflow

Read `references/ci-templates.md` for platform-specific CI templates. Pick the right template
based on project type:

- Desktop/KMP → Java + `./gradlew check`
- Android → Java + Android SDK + `./gradlew check`
- Multi-target → combined setup

If a CI workflow already exists, suggest adding `./gradlew check` as a step rather than
creating a new workflow.

#### Compose-driver — offer if Desktop or Android targets detected

compose-driver supports Desktop (Skiko virtual clock) and Android (Robolectric) targets.
If either is present, offer to set it up.

Read `references/compose-driver-setup.md` for setup instructions. Provide:
- Plugin declaration for `settings.gradle.kts`
- Target configuration (`desktop()`, `android()`, or both)
- Example test demonstrating the HTTP API
- CI additions (xvfb for Desktop, Robolectric config for Android)

If compose-driver would require significant build restructuring (e.g., no test infrastructure
at all yet), note this and let the user decide whether to defer it.

### Phase 4: Verify

After generating files, run verification:

```bash
./gradlew check
```

If detekt or ktfmt were newly added, there will likely be findings in existing code. This is
expected. Tell the user:

> "detekt/ktfmt found [N] findings in existing code. This is normal — the tools are now
> catching issues that weren't being checked before. You can address these incrementally.
> To create a baseline for existing findings: `./gradlew detektBaseline`"

Note: the baseline suggestion is specifically for the initial bootstrap of an existing codebase.
The generated agent instructions should instruct agents not to create or update baselines going
forward.

### Phase 5: Summary

Report what was generated, with file paths and a brief description of each. Highlight any
manual steps the user needs to take (e.g., adding plugin declarations to build files).

## Customization notes

The generated agent instructions reflect battle-tested practices from real Compose projects.
However, every team is different. After generation, the user should review and adjust:

- **TDD strictness**: The default is strict TDD (red before green). Teams not ready for this
  can soften it to "write tests for new features" without the red-first requirement.
- **Detekt thresholds**: The defaults are generous (LongMethod 100, TooManyFunctions 15).
  Tighten them as the codebase matures.
- **PR rules**: The default requires CI green before merge. Adjust if using a different
  merge strategy.
- **Worktree policy**: Useful for agent isolation but optional. Remove if the team doesn't
  use worktrees.
