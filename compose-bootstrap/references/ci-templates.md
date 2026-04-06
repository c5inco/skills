# CI Templates

This reference contains GitHub Actions workflow templates for different Compose project types.
Pick the template that matches the Phase 1 analysis, then customize.

## Desktop / KMP (JVM targets)

```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:

jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-java@v4
        with:
          distribution: jetbrains
          java-version: 21

      - uses: gradle/actions/setup-gradle@v4

      - run: ./gradlew check
```

## Android

```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:

jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-java@v4
        with:
          distribution: temurin
          java-version: 21

      - uses: gradle/actions/setup-gradle@v4

      - run: ./gradlew check

      # Optional: instrumented tests on an emulator
      # - uses: reactivecircus/android-emulator-runner@v2
      #   with:
      #     api-level: 34
      #     script: ./gradlew connectedCheck
```

## Compose Multiplatform (Desktop + Android)

```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:

jobs:
  check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-java@v4
        with:
          distribution: jetbrains
          java-version: 21

      - uses: gradle/actions/setup-gradle@v4

      - run: ./gradlew check
```

## Adding compose-driver E2E tests to CI

If compose-driver is configured, add a separate job for UI automation tests. Desktop
tests need a virtual framebuffer (xvfb). Android tests run via Robolectric (no display
needed).

```yaml
  e2e:
    runs-on: ubuntu-latest
    needs: check
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-java@v4
        with:
          distribution: jetbrains
          java-version: 21

      - uses: gradle/actions/setup-gradle@v4

      # Desktop: needs virtual framebuffer for Skiko rendering
      - name: Run compose-driver tests (Desktop)
        uses: coactions/setup-xvfb@v1
        with:
          run: ./gradlew test -PincludeTags=compose-driver

      # Android: Robolectric, no display needed
      # - run: ./gradlew test -PincludeTags=compose-driver-android
```

## Customization notes

1. **Java distribution**: Use `jetbrains` for Compose Desktop (required for Skiko). Use
   `temurin` for Android-only projects. For KMP with Desktop targets, use `jetbrains`.

2. **Runner**: `ubuntu-latest` works for most cases. For faster builds, consider
   self-hosted runners or paid options like Blacksmith or Namespace.

3. **Gradle caching**: `gradle/actions/setup-gradle@v4` handles caching automatically.

4. **Node.js**: Only add `actions/setup-node` if the project has npm dependencies
   (e.g., TypeScript extensions, web assets).

5. **Branch protection**: After CI is working, recommend the user enable branch
   protection rules requiring the `check` job to pass before merge.
