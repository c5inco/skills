# Compose-Driver Setup

This reference covers how to add compose-driver to a Compose project for UI test automation.
compose-driver exposes the running Compose UI as an HTTP API for taking screenshots, inspecting
the UI tree, clicking elements, and controlling the app programmatically.

## Supported platforms

- **Desktop (JVM)**: Uses Skiko virtual clock. Fast, headless-capable (with xvfb).
- **Android**: Uses Robolectric. No device/emulator needed.

## Setup steps

### 1. Add the plugin to settings.gradle.kts

```kotlin
plugins {
    // ... existing plugins ...
    id("io.github.jdemeulenaere.compose-driver") version "0.4.0"
}
```

### 2. Configure targets

In `settings.gradle.kts`, add the target configuration:

```kotlin
// Desktop only
composeDriver {
    desktop()
}

// Android only
composeDriver {
    android()
}

// Both
composeDriver {
    desktop()
    android()
}
```

### 3. Dependencies

compose-driver adds test dependencies automatically via the plugin. No manual dependency
declarations needed.

### 4. Writing a compose-driver test

compose-driver starts an HTTP server that exposes the UI tree. Tests interact with
the app through this HTTP API.

```kotlin
@Tag("compose-driver")
class MyComposeDriverTest {

    @Test
    fun `app launches and shows home screen`() {
        // compose-driver provides the test infrastructure
        // See compose-driver documentation for the full API:
        // - GET /screenshot — capture the current UI as PNG
        // - GET /tree — get the semantic tree as JSON
        // - POST /click — click at coordinates or on a node
        // - POST /input — type text into focused field
        // - POST /swipe — swipe gesture
    }
}
```

### 5. Running tests

```bash
# Desktop compose-driver tests
./gradlew test -PincludeTags=compose-driver

# With virtual framebuffer (CI / headless)
xvfb-run ./gradlew test -PincludeTags=compose-driver
```

### 6. CI integration

See `ci-templates.md` for the E2E job template with xvfb setup.

## When to recommend compose-driver

Recommend it when:
- The project has UI that would benefit from automated testing
- The team wants to catch UI regressions in CI
- Manual QA is a bottleneck

Defer it when:
- The project has no test infrastructure at all yet (set up unit tests first)
- The build is already complex and adding another plugin would be overwhelming
- The project is in early prototyping phase where UI changes rapidly

## Notes for the bootstrap skill

When adding compose-driver to a project:
1. Check that the Compose version is compatible (1.6+ recommended)
2. Add the test tag exclusion to the default test task so compose-driver tests don't
   run on every `./gradlew test`
3. Update TESTING.md with compose-driver examples
4. Update CI with the E2E job if GitHub Actions is being used
