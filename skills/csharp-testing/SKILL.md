---
name: csharp-testing
description: >
  C# and .NET testing patterns with xUnit, FluentAssertions, NSubstitute/Moq, AutoFixture, and WebApplicationFactory integration tests.
  Use when writing unit or integration tests in .NET, configuring test suites, or when user mentions "csharp-testing", "xunit",
  "fluentassertions", or "dotnet test".
argument-hint: "[xunit|fluentassertions|nsubstitute|integration|autofixture]"
license: MIT
---

# C# Testing — .NET Testing & Assertion Patterns

Based on [affaan-m/csharp-testing](https://skillrepo.dev/skills/affaan-m/csharp-testing) (v1.2A), this skill provides testing patterns for .NET applications.

## Standards

- **AAA Pattern**: Arrange, Act, Assert explicitly demarcated.
- **FluentAssertions**: Use readable assertions (`result.Should().BeEquivalentTo(expected);`).
- **WebApplicationFactory**: In-memory integration testing for API endpoints without real network ports.
