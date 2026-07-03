import os, re, json, glob
from collections import OrderedDict

CATEGORIES = {
    r'^(ab-testing|ad-creative|ads|analytics|aso|churn-prevention|co-marketing|community-marketing|cro|customer-research|email|free-tools|image|launch|lead-magnet|marketing-|onboarding|paywalls|popups|pricing|product-marketing|referrals|signup|ai-seo)': 'Marketing & Growth',
    r'^(video|hyperframes|gsap|waapi|animejs|lottie|three|css-animations|remotion|walkthrough-video|website-to-hyperframes)': 'Video & Animation',
    r'^(frontend-design|design|ui-ux|banner|brand|slides|ckm:|teach-impeccable|quieter|bolder|polish|overdrive|optimize|normalize|harden|extract|distill|delight|critique|colorize|clarify|arrange|animate|adapt|audit|typeset|onboard|color-palette|icon-set|favicon|design-system|design-review|landing-page|product-showcase|impeccable|critique)': 'Design & UX',
    r'^(python-pro|rust-engineer|golang-pro|csharp|dotnet|java-architect|spring-boot|nestjs|nextjs|react|vue|angular|flutter|swift|kotlin|php-pro|typescript-pro|javascript-pro|nodejs|fastapi|django|laravel|rails|sql-pro|pandas|database-optimizer|postgres|microservices|api-designer|graphql|websocket|backend|fullstack|code-reviewer|debugging|test-master|spec-miner|legacy-modernizer|architecture-designer|feature-forge|cli-developer|chaos-engineer|embedded-systems|game-developer|rag-architect|ml-pipeline|fine-tuning|prompt-engineer|mcp-developer)': 'Development & Backend',
    r'^(docker|devops|terraform|kubernetes|cloud-architect|sre|monitoring|cloudflare|d1-|d1-drizzle|hono-|vite-flare|tanstack|cloudflare-api|github-release|git-workflow|git-commit|cicd)': 'DevOps & Cloud',
    r'^(voltagent|composio|mcp-builder|elevenlabs|create-voltagent|nemoclaw|gws-|google-apps-script|google-chat|agent-browser)': 'AI & Agents',
    r'^(seo|keyword|schema|content-brief|content-gap|content-quality|content-refresher|on-page|technical-seo|meta-optimizer|rank-tracker|backlink|domain-authority|competitor-analysis|geo-content|ai-visibility|entity-optimizer|memory-management|alert-manager|performance-reporter|programmatic-seo|cannibalization|internal-link|site-architecture)': 'SEO & Content',
    r'^(cold-email|sales-enablement|proposal-writer|resume-cover-letter|award-application|strategy-document)': 'Sales & Comms',
    r'^(ln-|github-pr|github-merge|github-review)': 'Project Management',
    r'^(business-english|us-business-english|uk-business-english|aussie-business-english|nz-business-english|copy-editing|copywriting|content-strategy)': 'Writing & Content',
}

def parse_skill(path, repo_label):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    m = re.search(r'^---\s*\nname:\s*(.+?)\n', content, re.MULTILINE)
    name = m.group(1).strip() if m else os.path.basename(os.path.dirname(path))
    m = re.search(r'^description:\s*"(.+?)"', content, re.MULTILINE | re.DOTALL)
    desc = m.group(1).strip() if m else ''
    short = (desc[:120] + '...') if len(desc) > 120 else desc
    return name, short

base_dirs = [
    (os.path.expanduser('~/.agents/skills'), 'agents', '~/.agents/skills'),
    (os.path.expanduser('~/.config/opencode/skills'), 'opencode', '~/.config/opencode/skills'),
    (os.path.expanduser('~/.claude/skills'), 'claude', '~/.claude/skills'),
]

ORDER = {'agents': 0, 'opencode': 1, 'claude': 2}
skills = {}

for base, repo, prefix in base_dirs:
    if not os.path.isdir(base):
        continue
    for skill_file in glob.glob(os.path.join(base, '**', 'SKILL.md'), recursive=True):
        name, desc = parse_skill(skill_file, repo)
        rel = os.path.relpath(skill_file, os.path.dirname(base))
        rel = rel.replace('\\', '/')
        path = f'{prefix}/{rel}'
        if name not in skills or ORDER.get(repo, 9) < ORDER.get(skills[name]['repo'], 9):
            skills[name] = {'name': name, 'description': desc, 'path': path, 'repo': repo}

sorted_skills = sorted(skills.values(), key=lambda x: x['name'].lower())

categorized = OrderedDict()
for s in sorted_skills:
    cat = 'Other'
    for pattern, category in CATEGORIES.items():
        if re.search(pattern, s['name'], re.IGNORECASE):
            cat = category
            break
    categorized.setdefault(cat, []).append(s)
cat_order = ['Marketing & Growth', 'Video & Animation', 'Design & UX', 'Development & Backend',
             'DevOps & Cloud', 'AI & Agents', 'SEO & Content', 'Sales & Comms',
             'Project Management', 'Writing & Content', 'Other']

lines = []
lines.append('# Skills Index\n')
lines.append(f'Total unique skills: **{len(sorted_skills)}**\n')
lines.append('## Origin Repos\n')
lines.append('| Repo | Location | Count |')
lines.append('|------|----------|-------|')
for repo, label in [('agents', '~/.agents/skills/'), ('opencode', '~/.config/opencode/skills/'), ('claude', '~/.claude/skills/')]:
    count = sum(1 for s in sorted_skills if s['repo'] == repo)
    lines.append(f'| **{repo}** | `{label}` | {count} |')
lines.append('')
lines.append('---\n')
lines.append('## By Category\n')

for cat in cat_order:
    if cat not in categorized:
        continue
    items = categorized[cat]
    lines.append(f'### {cat} ({len(items)})\n')
    lines.append('| Skill | Description | Location |')
    lines.append('|-------|-------------|----------|')
    for s in items:
        lines.append(f'| **{s["name"]}** | {s["description"]} | `{s["path"]}` |')
    lines.append('')

lines.append('---\n')
lines.append('## All Skills (Alphabetical)\n')
lines.append('| # | Skill | Description | Origin |')
lines.append('|---|-------|-------------|--------|')
for i, s in enumerate(sorted_skills, 1):
    lines.append(f'| {i} | **{s["name"]}** | {s["description"]} | {s["repo"]} |')

output = '\n'.join(lines)
with open(os.path.expanduser('~/Documents/SKILLS-INDEX.md'), 'w', encoding='utf-8') as f:
    f.write(output)
print(f'Done. {len(sorted_skills)} skills written.')
