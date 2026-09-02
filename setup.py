#!/usr/bin/env python3
"""
Backward-compatible setup.py for SuperDuperSkills.
Prefer using `pip install .` with pyproject.toml for modern builds.
"""
from setuptools import setup, find_packages
import os
import re

# Read version from superduper_cli.py without importing it
version = "4.0.0"
cli_path = os.path.join(os.path.dirname(__file__), "scripts", "superduper_cli.py")
if os.path.isfile(cli_path):
    with open(cli_path, "r", encoding="utf-8") as f:
        match = re.search(r'__version__\s*=\s*["\']([^"\']+)["\']', f.read())
        if match:
            version = match.group(1)

# Read README
readme_path = os.path.join(os.path.dirname(__file__), "README.md")
long_description = ""
if os.path.isfile(readme_path):
    with open(readme_path, "r", encoding="utf-8") as f:
        long_description = f.read()

setup(
    name="superduperskills",
    version=version,
    description="The Ultimate Multi-Agent Skills Hub & Governance Suite — 2,700+ curated AI agent skills",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="camilolealdev",
    author_email="camilolealdev@users.noreply.github.com",
    url="https://superduperskills.vercel.app",
    project_urls={
        "Repository": "https://github.com/camilolealdev/superduperskills",
        "Bug Tracker": "https://github.com/camilolealdev/superduperskills/issues",
        "Documentation": "https://superduperskills.vercel.app",
    },
    license="MIT",
    python_requires=">=3.8",
    py_modules=["superduper_cli"],
    packages=[],
    scripts=[],
    entry_points={
        "console_scripts": [
            "sds=scripts.superduper_cli:main",
            "superduperskills=scripts.superduper_cli:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": [
            "completions/*.bash",
            "completions/*.zsh",
            "completions/*.fish",
            "skills/*/SKILL.md",
        ],
    },
    data_files=[
        ("share/bash-completion/completions", ["completions/sds.bash"]),
        ("share/zsh/site-functions", ["completions/sds.zsh"]),
        ("share/fish/vendor_completions.d", ["completions/sds.fish"]),
    ],
    keywords=[
        "ai", "skills", "agents", "claude-code", "gemini-cli",
        "cursor-rules", "agentic-ai", "yagni", "anti-slop",
        "prompt-engineering", "multi-agent",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Quality Assurance",
        "Topic :: Utilities",
    ],
)
