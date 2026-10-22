# Import Log

Skills imported from GitHub (shallow clones, SKILL.md dirs only; contents treated as untrusted data, nothing executed). Regex scan for prompt-injection / curl-pipe-sh patterns flagged 0 skills.
Apache-2.0 / MPL-2.0 / CC-BY-SA repos have their LICENSE copied into each skills/<name>/LICENSE.

| Repo | License | Skills added | Skipped + reason |
|---|---|---|---|
| vercel-labs/next-skills (old commit; moved to vercel/next.js) | none in repo at that commit | 3: next-best-practices, next-cache-components, next-upgrade |  |
| hashicorp/agent-skills | MPL-2.0 | 1: refactor-module |  |
| googleworkspace/cli | Apache-2.0 | 44 (see skills/ dirs) |  |
| dbt-labs/dbt-agent-skills | Apache-2.0 | 16: adding-dbt-unit-test, answering-natural-language-questions-with-dbt, building-dbt-semantic-layer, configuring-dbt-mcp-server, creating-mermaid-dbt-dag, fetching-dbt-docs, maintaining-dbt-documentation, migrating-dbt-core-to-v2, migrating-dbt-project-across-platforms, querying-the-dbt-information-schema, running-dbt-commands, troubleshooting-dbt-job-errors, upgrading-dbt, using-dbt-for-analytics-engineering, using-dbt-state, working-with-dbt-mesh |  |
| dash0hq/agent-skills | Apache-2.0 | 4: otel-collector, otel-instrumentation, otel-ottl, otel-semantic-conventions |  |
| trailofbits/skills | CC-BY-SA-4.0 | 1: differential-review |  |
| getsentry/sentry-agent-skills | none in repo (clone has no LICENSE) | 2: sentry-otel-exporter-setup, sentry-setup-ai-monitoring |  |
| trycourier/courier-skills | MIT | 1: courier |  |
| czlonkowski/n8n-skills | MIT | 0:  | 15 already present by name |
| serpapi/skills | MIT | 1: serpapi-web-search |  |
| w95/awesome-claude-corporate-skills | MIT | 126 (see skills/ dirs) | 39 already present by name |
| vercel-labs/skills | MIT | 0:  | find-skills (exists) |
| NVIDIA/SkillSpector | Apache-2.0 | 0:  | skill-inspector (exists) |
| hashicorp: terraform-style-guide, terraform-test, terraform-stacks, terraform-search-import | MPL-2.0 | 0 | not present in repo HEAD (only refactor-module exists) |
| trailofbits/skills: insecure-defaults | CC-BY-SA-4.0 | 0 | plugin has no SKILL.md (commands/references only) |
| netlify/context-and-tools (netlify-cli-and-deploy) | MIT | 0 | renamed upstream to netlify-deploy, which already exists in skills/ |
| getsentry/skills (requested sentry skills) | Apache-2.0 | 0 | sentry skills live in getsentry/sentry-agent-skills instead (see that row) |
| netlify/skills, SerpApi/serpapi-skill, getsentry (guessed names) | - | - | clone failed: repo not found (resolved to netlify/context-and-tools, serpapi/skills) |
