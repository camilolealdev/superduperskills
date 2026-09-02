#!/usr/bin/env python3
"""
Build script for superduperskills repo.
- Scans all skill repos, deduplicates by name
- Bundles SKILL.md files into skills/
- Generates SKILLS-INDEX.md with GitHub repo info
"""
import os, re, json, shutil, stat, subprocess
from pathlib import Path

BASE = os.path.dirname(os.path.abspath(__file__))
REPO_SKILLS = os.path.join(BASE, 'skills')

ORDER = {'agents': 0, 'opencode': 1, 'claude': 2}

SKILL_DIRS = [
    ('agents', os.path.expanduser('~/.agents/skills')),
    ('opencode', os.path.expanduser('~/.config/opencode/skills')),
    ('claude', os.path.expanduser('~/.claude/skills')),
]

GITHUB_URLS = {
    # git subdirectory -> GitHub URL (for opencode/claude repos)
    'backend-arch': 'https://github.com/levnikolaevich/claude-code-skills',
    'backend-skills': 'https://github.com/Jeffallan/claude-skills',
    'frontend-jezweb': 'https://github.com/jezweb/claude-skills',
    'impeccable': 'https://github.com/pbakaus/impeccable',
    'seo': 'https://github.com/ccforseo/seo-claude-code-skills',
    'seo-agrici': 'https://github.com/AgriciDaniel/claude-seo',
    'seo-ccforseo': 'https://github.com/ccforseo/seo-claude-code-skills',
    'seo-geo': 'https://github.com/aaron-he-zhu/seo-geo-claude-skills',
    'testcontainers': 'https://github.com/testcontainers/claude-skills',
    'ui-ux-pro-max': 'https://github.com/nextlevelbuilder/ui-ux-pro-max-skill',
    'git-cicd': 'https://github.com/fvadicamo/dev-agent-skills',
    'docker': 'https://github.com/wrsmith108/docker-claude-skill',
    # === NEW: high-star public repos ===
    'addyosmani': 'https://github.com/addyosmani/agent-skills',
    'taste': 'https://github.com/Leonxlnx/taste-skill',
    'design-taste-frontend': 'https://github.com/Leonxlnx/taste-skill',
    'design-taste-frontend-v1': 'https://github.com/Leonxlnx/taste-skill',
    'taste-skill-v1': 'https://github.com/Leonxlnx/taste-skill',
    'ponytail': 'https://github.com/DietrichGebert/ponytail',
    'ponytail-audit': 'https://github.com/DietrichGebert/ponytail',
    'ponytail-debt': 'https://github.com/DietrichGebert/ponytail',
    'ponytail-gain': 'https://github.com/DietrichGebert/ponytail',
    'ponytail-help': 'https://github.com/DietrichGebert/ponytail',
    'ponytail-review': 'https://github.com/DietrichGebert/ponytail',
    'planning-with-files': 'https://github.com/OthmanAdi/planning-with-files',
    'alirezarezvani': 'https://github.com/alirezarezvani/claude-skills',
    'drawio': 'https://github.com/Agents365-ai/drawio-skill',
    'prompt-architect': 'https://github.com/ckelsoe/claude-skill-prompt-architect',
    'prompt-coach': 'https://github.com/hancengiz/claude-code-prompt-coach-skill',
    'token-optimizer': 'https://github.com/severity1/claude-code-prompt-improver',
}

# Load skill-lock.json for agents GitHub URLs
AGENTS_GITHUB = {}
lock_path = os.path.expanduser('~/.agents/.skill-lock.json')
if os.path.isfile(lock_path):
    with open(lock_path) as f:
        lock = json.load(f)
    for name, info in lock.get('skills', {}).items():
        if info.get('sourceType') == 'github':
            url = info.get('sourceUrl', '').replace('.git', '').rstrip('/')
            AGENTS_GITHUB[name] = url

def get_git_remote(dir_path):
    try:
        r = subprocess.run(['git', 'remote', 'get-url', 'origin'],
                           cwd=dir_path, capture_output=True, text=True, timeout=5)
        if r.returncode == 0:
            return r.stdout.strip().replace('.git', '').rstrip('/')
    except:
        pass
    return ''

def parse_skill(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    front = re.search(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    name = os.path.basename(os.path.dirname(path))
    desc = ''
    if front:
        lines = front.group(1).split('\n')
        i = 0
        while i < len(lines):
            line = lines[i]
            if line.startswith('name:'):
                name = line.split(':', 1)[1].strip().strip('"\'')
            elif line.startswith('description:'):
                value = line.split(':', 1)[1].strip()
                if value in ('>', '>-', '>+', '|', '|-', '|+'):
                    # YAML block scalar: description text is on subsequent indented lines
                    block_lines = []
                    i += 1
                    while i < len(lines) and (lines[i].startswith((' ', '\t')) or not lines[i].strip()):
                        block_lines.append(lines[i].strip())
                        i += 1
                    i -= 1
                    desc = ' '.join(l for l in block_lines if l)
                else:
                    desc = value.strip('"\'')
            i += 1
    if len(desc) > 200:
        desc = desc[:197] + '...'
    desc = desc.replace('|', '\\|').replace('\n', ' ')
    return name, desc, content

# Collect all skills, deduplicate by name
skills = {}
for repo, base_dir in SKILL_DIRS:
    if not os.path.isdir(base_dir):
        print(f'Warning: {base_dir} not found, skipping')
        continue
    for fp in Path(base_dir).rglob('SKILL.md'):
        name, desc, content = parse_skill(str(fp))
        candidate_order = ORDER.get(repo, 9)
        candidate_richness = sum(1 for _ in fp.parent.rglob('*') if _.is_file())
        candidate_path = str(fp).replace('\\', '/')
        candidate_official = 'anthropics-skills' in candidate_path or 'claude-plugins-official' in candidate_path
        if name not in skills:
            take_it = True
        else:
            existing_order = ORDER.get(skills[name]['repo'], 9)
            existing_official = skills[name].get('official', False)
            if candidate_order != existing_order:
                take_it = candidate_order < existing_order
            elif candidate_official != existing_official:
                # First-party Anthropic skills win ties over third-party repos
                # that happen to reuse the same generic skill name.
                take_it = candidate_official
            else:
                # Same priority tier: prefer whichever copy has more supporting
                # files, so the pick is deterministic regardless of directory
                # scan order (which shifts whenever sibling dirs are added).
                take_it = candidate_richness > skills[name].get('richness', 0)
        if take_it:
            rel = os.path.relpath(str(fp.parent), base_dir)
            rel = rel.replace('\\', '/')

            # Determine GitHub URL
            github_url = ''
            if repo == 'agents':
                github_url = AGENTS_GITHUB.get(name, '')
            else:
                # Try matching subdirectory in GITHUB_URLS
                top_dir = rel.split('/')[0] if '/' in rel else rel
                if top_dir and top_dir in GITHUB_URLS:
                    github_url = GITHUB_URLS[top_dir]
                elif name in GITHUB_URLS:
                    github_url = GITHUB_URLS[name]

            # Also try git remote as fallback for opencode/claude
            if not github_url and repo in ('opencode', 'claude'):
                skill_dir = str(fp.parent)
                # Walk up to find a .git dir
                d = skill_dir
                while d and d != base_dir and len(d) > len(base_dir):
                    if os.path.isdir(os.path.join(d, '.git')):
                        github_url = get_git_remote(d)
                        break
                    d = os.path.dirname(d)

            dir_name = re.sub(r'[<>:"/\\|?*]', '-', name)

            skills[name] = {
                'name': name,
                'dir_name': dir_name,
                'description': desc,
                'rel_path': f'{rel}/SKILL.md',
                'repo': repo,
                'github_url': github_url,
                'source_dir': str(fp.parent),
                'richness': candidate_richness,
                'official': candidate_official,
                'content': content,
            }

# Write skills to repo — mirror the whole skill directory (SKILL.md plus any
# references/scripts/assets), not just SKILL.md, so supporting files survive.
os.makedirs(REPO_SKILLS, exist_ok=True)
ignore_git = shutil.ignore_patterns('.git')
def _is_link_or_junction(path):
    """True for symlinks and Windows NTFS junctions (mount-point reparse
    points). shutil.rmtree refuses both, so callers must unlink() instead."""
    try:
        st = os.lstat(path)
    except OSError:
        return False
    if stat.S_ISLNK(st.st_mode):
        return True
    attrs = getattr(st, 'st_file_attributes', 0)
    return bool(attrs & getattr(stat, 'FILE_ATTRIBUTE_REPARSE_POINT', 0))

for name, data in skills.items():
    dest_dir = os.path.join(REPO_SKILLS, data['dir_name'])
    if _is_link_or_junction(dest_dir):
        # Junction/symlink (e.g. from `npx skills add`): unlink the link
        # itself, never rmtree through it into whatever it points at.
        os.rmdir(dest_dir)
    elif os.path.isdir(dest_dir):
        shutil.rmtree(dest_dir)
    shutil.copytree(data['source_dir'], dest_dir, ignore=ignore_git)

# Generate SKILLS-INDEX.md
sorted_skills = sorted(skills.values(), key=lambda x: x['name'].lower())

CATEGORIES = [
    (r'^(ab-testing|ad-creative|ads|analytics|aso|churn-prevention|co-marketing|community-marketing|cro|customer-research|emails?|free-tools|image|launch|lead-magnet|marketing-|onboarding|paywalls|popups?|pricing|product-marketing|referrals?|signup|ai-seo|app-store-optimization|paid-ads|page-cro|form-cro|paywall-upgrade-cro|^promote$|scorecard-marketing|serp-analysis|^social$|social-content|x-twitter-growth|youtube-full|substack-expert|webinar-marketing|geo-optimization|meta-tags-optimizer|local-seo-manager|directory-submissions|campaign-analytics|intl-expansion|rfp-responder|contract-and-proposal-writer|market-research|storybrand-messaging|made-to-stick|one-page-marketing|obviously-awesome|monetizing-innovation|jobs-to-be-done|hundred-million-offers|predictable-revenue|influence-psychology|cold-start-problem|^contagious$|blue-ocean-strategy|good-strategy-bad-strategy|lean-analytics|lean-startup|inspired-product|continuous-discovery|mom-test|negotiation)', 'Marketing & Growth'),
    (r'^(video|hyperframes|gsap|waapi|animejs|lottie|three|css-animations|remotion-to-hyperframes|walkthrough-video|website-to-hyperframes|hyperframes-)', 'Video & Animation'),
    (r'^(frontend-design|design|design-taste|ui-ux|banner|brand|slides|ckm:|teach-impeccable|quieter|bolder|polish|overdrive|optimize|normalize|harden|extract|distill|delight|critique|colorize|clarify|arrange|animate|adapt|audit|typeset|onboard|color-palette|icon-set|favicon|design-system|design-review|landing-page|product-showcase|impeccable|taste-|brandkit|imagegen-|a11y-|high-end-visual|minimalist-ui|industrial-brutalist|stitch-design|ponytail|awesome-design-md|baseline-ui|canvas-design|create-design-md|drawio-skill|excalidraw-diagram|fixing-accessibility|fixing-metadata|fixing-motion-performance|frontend-dev-guidelines|frontend-ui-engineering|gpt-taste|hooked-ux|improve-ui|ios-hig-design|apple-hig-expert|^landing$|microinteractions|migrate-design-system|mermaidjs|refactoring-ui|responsiveness-check|shadcn-ui|steve-jobs-design-review|^tailwind|theme-factory|top-design|ui-design-system|ui-skills-root|ui-styling|ultimate-design-system-master|ux-audit|ux-heuristics|ux-researcher-designer|ux-writing|vercel-react-best-practices|web-artifacts-builder|web-design-guidelines|web-typography|astro|^aesthetic$|apply-aesthetic)', 'Design & UX'),
    (r'^(python-pro|rust-engineer|golang-pro|csharp|dotnet|java-architect|spring-boot|nestjs|nextjs|react|vue|angular|flutter|swift|kotlin|php-pro|typescript-pro|javascript-pro|nodejs|fastapi|django|laravel|rails|sql-pro|pandas|database-optimizer|postgres|microservices|api-designer|graphql|websocket|backend|fullstack|code-reviewer|debugging|test-master|spec-miner|legacy-modernizer|architecture-designer|feature-forge|cli-developer|chaos-engineer|embedded-systems|game-developer|rag-architect|ml-pipeline|fine-tuning|prompt-engineer|mcp-developer|playwright-expert|atlassian-mcp|fastapi-expert|api-|code-|cicd|ci-cd|browser-testing|frontend-engineering|fullstack-|observability|security-|database-|schema-|performance-|testing-|debug-|source-driven|doubt-driven|test-driven|incremental|spec-driven|shipping|source-code|adversarial-reviewer|interview-me|ai-security|encryption|caching-|orm-|migration-|open-source|app-development|mobile-development|game-development|engineering|cmd-|grill-|karpathy|senior-|better-auth|auth-md|auth-patterns|cpp-pro|salesforce-developer|sql-database-assistant|stripe-integration-expert|stripe-payments|^supabase|prisma-workflow|typescript-patterns|shopify|wordpress|snowflake-development|spark-engineer|feature-flags-architect|tech-stack-evaluator|deployment-guide|payment-integration|media-processing|markdown-html-orchestrator|okf-open-knowledge-format|obsidian-vault|ms365-tenant-manager|jira-expert|confluence-expert)', 'Development & Backend'),
    (r'^(docker|devops|terraform|kubernetes|cloud-architect|sre|monitoring|cloudflare|d1-|d1-drizzle|hono-|vite-flare|tanstack-start|cloudflare-api|github-release|git-workflow|git-commit|cicd|github-|git-|container|aws-|azure-|gcp-|cloud-|deploy-|infrastructure|incident-management|disaster-recovery|load-testing|incident|helm-chart-builder|runbook-generator|coolify-operator|^bunny$|pier-cloud|env-secrets-manager|secrets-vault-manager|^deploy$|netlify-deploy|render-deploy|vercel-deploy|python-appservice-deploy|teams-app-developer|agents-sdk|sandbox-sdk|durable-objects|^wrangler$|workers-best-practices|turnstile-spin|copilot-sdk|debugview|appinsights-instrumentation|applicationinsights-web-ts|aspnet-core|winui-app|airunway-aks-setup|install-atk)', 'DevOps & Cloud'),
    (r'^(voltagent|composio|mcp-builder|elevenlabs|create-voltagent|nemoclaw|gws-|google-apps-script|google-chat|agent-browser|prompt-architect|prompt-improver|pinokio|agent-|ai-|llm|rag|chatbot|autonomous|autoresearch|google-|atlassian|agenthub|flow-nexus|swarm|sequential-thinking|mcp-management|mcp-server-builder|context-engine|docs-seeker|deep-research|research-|repomix|notebooklm|^browser$|browser-automation|chrome-devtools|high-perf-browser|claude-api|^claude-code$|claude-coach|zero-hallucination-coder|universal-scraping-architect|workflow-builder|^figma$|^linear$|^sentry$|jupyter-notebook|^kql$|pydantic-models-py|langsmith-fetch|openai-docs|chatgpt-apps|declarative-agent-developer|^openclaw$|knowledge-agent|smart-explore|continual-learning|memory-review|memory-status|mem-search|reasoningbank|agentdb)', 'AI & Agents'),
    (r'^(seo|keyword|schema|content-brief|content-gap|content-quality|content-refresher|on-page|technical-seo|meta-optimizer|rank-tracker|backlink|domain-authority|content-auditor|competitor-analysis|geo-content|ai-visibility|entity-optimizer|memory-management|alert-manager|performance-reporter|programmatic-seo|cannibalization|internal-link|site-architecture|aeo)', 'SEO & Content'),
    (r'^(cold-email|sales-enablement|proposal-writer|resume-cover-letter|award-application|strategy-document|sales-|pitch-deck|investor-|fundraising|cold-calling)', 'Sales & Comms'),
    (r'^(ln-|task-|todo|planning-|pi-planning|idea-refine|context-engineering|using-agent-skills|doc-|documentation|meeting-|standup|retrospective|daily-|weekly-|sprint-|backlog|roadmap|stakeholder)', 'Project Management'),
    (r'^(us-business-english|uk-business-english|aussie-business-english|nz-business-english|copy-editing|copywriting|content-strategy|cs-|content-|blog-|article-|newsletter|social-media|copy-|email-|messaging|internal-comms|wiki-|changelog|release-notes|md$|md-|inbox)', 'Writing & Content'),
    (r'^(board|boardroom|chief-|ceo-|cto-|cfo-|cmo-|coo-|cpo-|ciso|c-level|founder-|business-|strategy-|revenue-|finance-|financial-|commercial|startup|competitive|product-|pm-|growth|lob-|enterprise|corporate|competitor|caio-review|cco-review|cdo-review|gc-review|vpe-advisor|vpe-review|chro-advisor|general-counsel-advisor|skills-chief-|skills-general-counsel-advisor|skills-vpe-advisor|executive-mentor|decision-logger|org-health-diagnostic|company-os|ma-playbook|deal-desk|procurement-optimizer|partnerships-architect|vendor-management|^revops$|scenario-war-room|high-output-management|drive-motivation|team-communications|team-update|brains-trust|^challenge$|hard-call|the-fool|arquiteto-de-empresa|capacity-planner|^okr$|solo-founder|statistical-analyst|strategic-alignment|^tc$|tc-tracker|saas-health|saas-metrics-coach|scrum-master|operator-audit|office-hours|^patent$|^rice$|create-app|create-business|create-website|grow-app|grow-business|grow-website|improve-app|improve-business|improve-website|improve-retention|billion-dollar-ai-team|customer-success-manager|channel-economics|change-management|capacity$|deep-work|define-goal|fable-goal|make-plan|traction-eos|37signals-way|ddia-systems|developer-growth-analysis)', 'Business & Strategy'),
    (r'^(compliance|gdpr|ccpa|hippa|fda|soc-|iso-|legal-|ai-act|regulation|policy|risk-|audit-|governance|data-privacy|data-protection|eu-ai-act-specialist|isms-audit-expert|iso13485-audit-prep|iso27001-audit-prep|iso42001-specialist|soc2-audit-prep|soc2-compliance|information-security-manager-iso27001|mdr-745-specialist|qms-audit-expert|quality-manager-qmr|quality-manager-qms-iso13485|ra-qm-skills|regulatory-affairs-head|threat-detection|owasp-security|secure-code-guardian|plugin-audit|dependency-auditor|data-quality-auditor|aims-audit|clinical-research)', 'Compliance & Legal'),
    (r'^(loop-|md-|inbox-|andreessen|behuman|full-|brainstorm|career|hiring|recruiting|hr-|people-|culture|onboarding-|training|learning-|mentoring|coaching)', 'Productivity & People'),
    (r'^(qe-|qcsd-|test-|^tdd$|tdd-guide|tdd-london-chicago|strict-tdd|mutation-testing|contract-testing|^coverage$|coverage-drop-investigator|coverage-guard|exploratory-testing|context-driven-testing|compatibility-testing|localization-testing|mobile-testing|holistic-testing|middleware-testing|visual-testing|webapp-testing|web-testing|^vitest$|playwright-pro|^pw$|skill-tester|skill-evaluation|sherlock-review|shift-left-testing|shift-right-testing|regression-testing|pentest-validation|^qa$|e2e-flow-verifier|diagnosing-bugs|systematic-debugging|root-cause|^no-skip$|freeze-tests|stress-test|testcontainers|testrail|debug-loop|n8n-.*-testing)', 'Testing & QA'),
    (r'^(ring:|ring-|pragmatic-programmer|clean-code|clean-architecture|domain-driven-design|domain-modeling|refactoring-patterns|working-with-legacy-code|software-design-philosophy|^system-design$|codebase-design|codebase-onboarding|monorepo-navigator|^tech-debt|remove-technical-debt|improve-codebase-architecture|ubiquitous-language|team-topologies|xp-practices|sparc-methodology|^wayfinder$|^implement$|^prototype$|spec-to-repo|^to-spec$|^to-tickets$|^to-questionnaire$|request-refactor-plan|resolving-merge-conflicts|^pr-review|^handoff$|claude-handoff|batch-grill-me|^grilling$|^ask-matt$|setup-matt-pocock|writing-great-skills|write-a-skill|skill-creator|skill-builder|skill-security-auditor|skill-stats|creating-skills|find-skills|template-skill|sample-skill|^init$|^setup$|^spawn$|^run$|^execute$|^fix$|focused-fix|^decide$|^reflect$|^remember$|self-eval|self-improving-agent|^loop$|iterative-loop|^merge$|^generate$|^report$|^status$|^roast$|^teach$|^wizard$|^caveman|cavecrew|^token-build$|^token-efficiency$|^token-savings$|^tokensaver$|systematic-debugging|root-cause-tracing|collision-zone-thinking|defense-in-depth-validation|inversion-exercise|meta-pattern-recognition|simplification-cascades|scale-game|when-stuck|brutal-honesty-review|verification-before-completion|verification-.-quality-assurance|slop-eval|skillopt-sleep|ralph-loop|migrate-to-codex|migrate-to-shoehorn|learn-codebase|pathfinder|problem-solving$|what-the|yeet|hatch-pet|raffle-winner-picker|babysit)', 'Engineering Practices'),
    (r'(-automation$| Automation$)|^(figma-|notion-|slack-|m365-|microsoft-|entra-|gh-|connect-apps|zapier|make-com)', 'Integrations & Automation'),
]

def categorize(name):
    for pat, cat in CATEGORIES:
        if re.search(pat, name, re.IGNORECASE):
            return cat
    return 'Other'

categorized = {}
for s in sorted_skills:
    cat = categorize(s['name'])
    categorized.setdefault(cat, []).append(s)

cat_order = ['Marketing & Growth', 'Video & Animation', 'Design & UX', 'Development & Backend',
             'Testing & QA', 'Engineering Practices', 'DevOps & Cloud', 'AI & Agents',
             'Integrations & Automation', 'SEO & Content', 'Sales & Comms', 'Project Management',
             'Writing & Content', 'Business & Strategy', 'Compliance & Legal',
             'Productivity & People', 'Other']

lines = [
    '# Skills Index\n',
    f'Total unique skills: **{len(sorted_skills)}**\n',
    '## Origin Repos\n',
    '| Repo | Location | Count |',
    '|------|----------|-------|',
]
for repo_name, label in [('agents', '~/.agents/skills/'), ('opencode', '~/.config/opencode/skills/'), ('claude', '~/.claude/skills/')]:
    count = sum(1 for s in sorted_skills if s['repo'] == repo_name)
    lines.append(f'| **{repo_name}** | `{label}` | {count} |')
lines.extend(['', '---', ''])

lines.append('## By Category\n')
for cat in cat_order:
    if cat not in categorized:
        continue
    items = categorized[cat]
    lines.append(f'### {cat} ({len(items)})\n')
    lines.append('| Skill | Description | GitHub | Location |')
    lines.append('|-------|-------------|--------|----------|')
    for s in items:
        gh = f'`{s["github_url"]}`' if s['github_url'] else ''
        lines.append(f'| **{s["name"]}** | {s["description"]} | {gh} | `skills/{s["dir_name"]}/SKILL.md` |')
    lines.append('')

lines.append('---\n')
lines.append('## All Skills (Alphabetical)\n')
lines.append('| # | Skill | Description | GitHub | Origin |')
lines.append('|---|-------|-------------|--------|--------|')
for i, s in enumerate(sorted_skills, 1):
    gh = s['github_url'] if s['github_url'] else '-'
    lines.append(f'| {i} | **{s["name"]}** | {s["description"]} | {gh} | {s["repo"]} |')

with open(os.path.join(BASE, 'SKILLS-INDEX.md'), 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print(f'Done. {len(sorted_skills)} skills bundled into skills/')
print(f'SKILLS-INDEX.md updated.')
