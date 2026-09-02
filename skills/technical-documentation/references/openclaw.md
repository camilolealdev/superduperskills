# OpenClaw Documentation Overlay

Use this reference only for OpenClaw docs work. It layers OpenClaw-specific page
types, navigation, preservation, and validation rules on top of the general
technical-documentation skill.

## Reader Model

- Lead with the task the reader is trying to complete.
- Give one recommended path before alternatives.
- Keep main docs focused on the common path; move dense contracts and rare
  debugging detail to linked reference or troubleshooting pages.
- Explain production risks exactly where the reader can make the mistake.
- Link concepts, guides, references, CLI pages, SDK docs, testing, and
  troubleshooting so readers can continue without rereading.

## Page Types

Choose the page type before writing or reviewing:

- Overview: route readers to the right product area, integration path, or guide.
- Quickstart: get a new user to a working result with the fewest safe steps.
- Topic page: explain a major OpenClaw entity or surface end to end.
- Guide: walk through one workflow from prerequisites to production readiness.
- API/SDK/CLI reference: define every object, method, command, option, response,
  error, enum, default, and version rule in scope.
- Testing guide: show sandbox setup, fixtures, simulated failures, and live-mode
  differences.
- Troubleshooting guide: map observable symptoms to checks, causes, and fixes.
- Governance file: keep agent/contributor policy concrete, scoped, and aligned
  with current OpenClaw repo behavior.

## Topic Pages

Use this shape for major-entity pages:

1. Title naming the entity or surface.
2. Unheaded opening that says what it is, what it owns, and what it does not own.
3. Requirements, only when setup needs accounts, versions, permissions, plugins,
   operating systems, or credentials.
4. Quickstart with the recommended path and smallest reliable verification.
5. Configuration with task-critical options inline and exhaustive details linked
   to reference docs.
6. Major subtopics organized by reader intent, not under a generic "Subtopics"
   heading.
7. Troubleshooting with observable failures and concrete checks.
8. Related links to guides, references, commands, concepts, and adjacent topics.

## Guides

Use this shape for workflow pages:

1. Title naming the outcome, not the implementation detail.
2. Opening that states what the reader can accomplish.
3. Before you begin: accounts, keys, permissions, versions, tools, and
   assumptions.
4. Choose a path, only when the reader must decide.
5. Steps with verb-led headings, commands, expected output, and checks.
6. Test with verification steps before finalizing.
