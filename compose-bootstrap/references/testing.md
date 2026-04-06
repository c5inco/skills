# Testing Template (docs/TESTING.md)

This reference contains the template for the testing conventions doc. Select the right
framework examples based on Phase 1 analysis.

## Template

```markdown
# Testing

## TDD Cycle

Every new feature or bug fix follows the TDD cycle:

1. **Write the test** — describe the expected behavior in a test method.
2. **Run it** — confirm it fails (red). The failure should be an assertion failure, not a
   compilation error.
3. **Implement** — write the minimum production code to make the test pass.
4. **Run again** — confirm it passes (green).
5. **Refactor** — clean up if needed, keeping tests green.

The test proves the implementation works. The red step proves the test is actually checking
something meaningful — a test that never fails is worthless.

{{Select the appropriate framework section(s) based on Phase 1:}}

## Test Frameworks

### Unit Tests (JUnit 5)

\`\`\`kotlin
@Test
fun `descriptive name of what is being tested`() = runTest {
    // Given
    val repository = FakeRepository()
    val viewModel = MyViewModel(repository)

    // When
    viewModel.loadData()

    // Then
    assertEquals(expected, viewModel.state.value.data)
}
\`\`\`

{{If JUnit 4 detected instead, use @Test from org.junit and @RunWith}}

### Compose UI Tests

{{For Desktop:}}
\`\`\`kotlin
@Test
fun `button click updates counter`() = runComposeUiTest {
    setContent {
        CounterScreen()
    }

    onNodeWithText("Count: 0").assertExists()
    onNodeWithText("Increment").performClick()
    onNodeWithText("Count: 1").assertExists()
}
\`\`\`

{{For Android:}}
\`\`\`kotlin
@get:Rule
val composeTestRule = createComposeRule()

@Test
fun buttonClickUpdatesCounter() {
    composeTestRule.setContent {
        CounterScreen()
    }

    composeTestRule.onNodeWithText("Count: 0").assertExists()
    composeTestRule.onNodeWithText("Increment").performClick()
    composeTestRule.onNodeWithText("Count: 1").assertExists()
}
\`\`\`

## Test Tags

Use JUnit 5 tags to categorize tests for selective CI execution:

\`\`\`kotlin
@Tag("slow")
@Test
fun `integration test that hits the database`() { ... }

@Tag("ui")
@Test
fun `compose ui test`() { ... }
\`\`\`

Run specific tags:
\`\`\`bash
./gradlew test -PincludeTags=ui
\`\`\`

Exclude tags from default runs in build.gradle.kts:
\`\`\`kotlin
tasks.test {
    useJUnitPlatform {
        excludeTags("slow", "ui")
    }
}
\`\`\`

## Test Placement

| Type | Location |
|------|----------|
| Unit tests | `src/test/kotlin/` (same package as production code) |
| Compose UI tests | `src/test/kotlin/` (Desktop) or `src/androidTest/kotlin/` (Android) |
| Integration / E2E | `src/test/kotlin/.../e2e/` or `src/androidTest/kotlin/` |
| Test fixtures | `src/test/kotlin/.../fixtures/` or `testFixtures/` source set |

## What to Test

Prioritize tests for:
- **Business logic** — state machines, reducers, transformations, validation
- **Data mapping** — serialization/deserialization, model conversions
- **Edge cases** — empty inputs, error states, boundary values
- **Regressions** — any bug fix should have a test that reproduces the bug

Lower priority:
- Trivial getters/setters
- Platform boilerplate (Activity lifecycle, service binding)
- UI layout details (prefer snapshot tests or manual verification)
```

## Customization guidance

1. **Framework selection**: Generate examples for the framework(s) actually in use. Don't
   include JUnit 5 examples if the project uses JUnit 4 or Kotest.

2. **Compose UI test variant**: Desktop uses `runComposeUiTest` (no Rule needed). Android
   uses `createComposeRule()` or `createAndroidComposeRule()`. KMP may have both.

3. **Coroutine testing**: If `kotlinx-coroutines-test` is in dependencies, include `runTest`
   examples. Otherwise use basic test patterns.

4. **compose-driver**: If compose-driver is being set up, add a section on E2E testing via
   the HTTP API. Read the compose-driver skill for examples.

5. **Test tags**: Suggest tags that make sense for the project. Common ones:
   - `slow` — tests that take >1s
   - `ui` — Compose UI tests requiring a display
   - `e2e` — end-to-end tests
   - `integration` — tests requiring external dependencies
