#!/usr/bin/env python3
"""
Build script for superduperskills repo.
- Scans all skill repos, deduplicates by name
- Bundles SKILL.md files into skills/
- Generates SKILLS-INDEX.md with GitHub repo info
"""
import os, re, json, shutil, subprocess
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
        if name not in skills or ORDER.get(repo, 9) < ORDER.get(skills[name]['repo'], 9):
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
                'content': content,
            }

# Write skills to repo
os.makedirs(REPO_SKILLS, exist_ok=True)
for name, data in skills.items():
    dest_dir = os.path.join(REPO_SKILLS, data['dir_name'])
    os.makedirs(dest_dir, exist_ok=True)
    with open(os.path.join(dest_dir, 'SKILL.md'), 'w', encoding='utf-8') as f:
        f.write(data['content'])

# Generate SKILLS-INDEX.md
sorted_skills = sorted(skills.values(), key=lambda x: x['name'].lower())

CATEGORIES = [
    (r'^(ab-testing|ad-creative|ads|analytics|aso|churn-prevention|co-marketing|community-marketing|cro|customer-research|emails?|free-tools|image|launch|lead-magnet|marketing-|onboarding|paywalls|popups?|pricing|product-marketing|referrals?|signup|ai-seo|app-store-optimization)', 'Marketing & Growth'),
    (r'^(video|hyperframes|gsap|waapi|animejs|lottie|three|css-animations|remotion-to-hyperframes|walkthrough-video|website-to-hyperframes|hyperframes-)', 'Video & Animation'),
    (r'^(frontend-design|design|design-taste|ui-ux|banner|brand|slides|ckm:|teach-impeccable|quieter|bolder|polish|overdrive|optimize|normalize|harden|extract|distill|delight|critique|colorize|clarify|arrange|animate|adapt|audit|typeset|onboard|color-palette|icon-set|favicon|design-system|design-review|landing-page|product-showcase|impeccable|taste-|brandkit|imagegen-|a11y-|high-end-visual|minimalist-ui|industrial-brutalist|stitch-design|ponytail)', 'Design & UX'),
    (r'^(python-pro|rust-engineer|golang-pro|csharp|dotnet|java-architect|spring-boot|nestjs|nextjs|react|vue|angular|flutter|swift|kotlin|php-pro|typescript-pro|javascript-pro|nodejs|fastapi|django|laravel|rails|sql-pro|pandas|database-optimizer|postgres|microservices|api-designer|graphql|websocket|backend|fullstack|code-reviewer|debugging|test-master|spec-miner|legacy-modernizer|architecture-designer|feature-forge|cli-developer|chaos-engineer|embedded-systems|game-developer|rag-architect|ml-pipeline|fine-tuning|prompt-engineer|mcp-developer|playwright-expert|atlassian-mcp|fastapi-expert|api-|code-|cicd|ci-cd|browser-testing|frontend-engineering|fullstack-|observability|security-|database-|schema-|performance-|testing-|debug-|source-driven|doubt-driven|test-driven|incremental|spec-driven|shipping|source-code|adversarial-reviewer|interview-me|ai-security|encryption|caching-|orm-|migration-|open-source|app-development|mobile-development|game-development|engineering|cmd-|grill-|karpathy)', 'Development & Backend'),
    (r'^(docker|devops|terraform|kubernetes|cloud-architect|sre|monitoring|cloudflare|d1-|d1-drizzle|hono-|vite-flare|tanstack-start|cloudflare-api|github-release|git-workflow|git-commit|cicd|github-|git-|container|aws-|azure-|gcp-|cloud-|deploy-|infrastructure|incident-management|disaster-recovery|load-testing|incident)', 'DevOps & Cloud'),
    (r'^(voltagent|composio|mcp-builder|elevenlabs|create-voltagent|nemoclaw|gws-|google-apps-script|google-chat|agent-browser|prompt-architect|prompt-improver|pinokio|agent-|ai-|llm|rag|chatbot|autonomous|autoresearch|google-|atlassian)', 'AI & Agents'),
    (r'^(seo|keyword|schema|content-brief|content-gap|content-quality|content-refresher|on-page|technical-seo|meta-optimizer|rank-tracker|backlink|domain-authority|content-auditor|competitor-analysis|geo-content|ai-visibility|entity-optimizer|memory-management|alert-manager|performance-reporter|programmatic-seo|cannibalization|internal-link|site-architecture|aeo)', 'SEO & Content'),
    (r'^(cold-email|sales-enablement|proposal-writer|resume-cover-letter|award-application|strategy-document|sales-|pitch-deck|investor-|fundraising|cold-calling)', 'Sales & Comms'),
    (r'^(ln-|task-|todo|planning-|pi-planning|idea-refine|context-engineering|using-agent-skills|doc-|documentation|meeting-|standup|retrospective|daily-|weekly-|sprint-|backlog|roadmap|stakeholder)', 'Project Management'),
    (r'^(us-business-english|uk-business-english|aussie-business-english|nz-business-english|copy-editing|copywriting|content-strategy|cs-|content-|blog-|article-|newsletter|social-media|copy-|email-|messaging|internal-comms|wiki-|changelog|release-notes|md$|md-|inbox)', 'Writing & Content'),
    (r'^(board|boardroom|chief-|ceo-|cto-|cfo-|cmo-|coo-|cpo-|ciso|c-level|founder-|business-|strategy-|revenue-|finance-|financial-|commercial|startup|competitive|product-|pm-|growth|lob-|enterprise|corporate|competitor)', 'Business & Strategy'),
    (r'^(compliance|gdpr|ccpa|hippa|fda|soc-|iso-|legal-|ai-act|regulation|policy|risk-|audit-|governance|data-privacy|data-protection)', 'Compliance & Legal'),
    (r'^(loop-|md-|inbox-|andreessen|behuman|full-|brainstorm|career|hiring|recruiting|hr-|people-|culture|onboarding-|training|learning-|mentoring|coaching)', 'Productivity & People'),
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
             'DevOps & Cloud', 'AI & Agents', 'SEO & Content', 'Sales & Comms',
             'Project Management', 'Writing & Content', 'Business & Strategy',
             'Compliance & Legal', 'Productivity & People', 'Other']

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
