#!/usr/bin/env python3
"""Shape check for the bilingual documentation standard.

    python3 check-docs.py [repo-path]

Deliberately shallow: it checks presence and shape, not truth.
Exit 0 = the repo has the skeleton; exit 1 = a listed check failed.
"""
from __future__ import annotations

import os
import re
import sys

EN_SECTIONS = {
    "what": r"(what it is|at a glance|overview)",
    "run": r"(run it|local environment|getting started|install|usage)",
    "verify": r"(verify|verifying|testing|gates|checks)",
}
FA_SECTIONS = {
    "چیست": r"(در یک نگاه|چیست|معرفی)",
    "اجرا": r"(اجرا|محیط|نصب|شروع|راه‌اندازی)",
    "بررسی": r"(بررسی|تست|گیت|آزمون)",
}
SECRETS = [
    (re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}"), "GitHub token"),
    (re.compile(r"\bsk-[A-Za-z0-9]{20,}"), "API key (sk-…)"),
    (re.compile(r"(?i)\b(password|passwd|api[_-]?key|secret)\s*[:=]\s*[\"'][^\"']{8,}[\"']"), "inline credential"),
]
SECRET_SKIP = re.compile(r"(?i)example|placeholder|dummy|redacted|your[_-]|xxx|<[^>]+>|change[_-]?me")

SKIP_DIRS = {".git", "node_modules", ".venv", "dist", "build", "__pycache__", ".verify"}


def read(path: str) -> str:
    with open(path, encoding="utf-8", errors="replace") as fh:
        return fh.read()


def headings(text: str) -> list[str]:
    return [ln for ln in text.splitlines() if ln.startswith("#")]


def walk(root: str):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for name in filenames:
            yield os.path.join(dirpath, name)


def check_sections(label: str, text: str, wanted: dict[str, str], problems: list[str]) -> None:
    heads = "\n".join(headings(text)).lower()
    for title, pattern in wanted.items():
        if not re.search(pattern, heads, re.IGNORECASE):
            problems.append(f"{label}: no heading for «{title}» (looked for /{pattern}/)")


def check_mermaid(label: str, text: str, problems: list[str]) -> None:
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.strip().startswith("```mermaid"):
            rest = [ln.strip() for ln in lines[i + 1:]]
            if not any(ln.startswith("```") for ln in rest):
                problems.append(f"{label}: mermaid block at line {i + 1} is never closed")
            return


def main() -> int:
    root = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else ".")
    problems: list[str] = []

    en_path = os.path.join(root, "README.md")
    fa_path = os.path.join(root, "README.fa.md")
    for path in (en_path, fa_path):
        if not os.path.isfile(path):
            problems.append(f"missing {os.path.relpath(path, root)}")
    if problems:
        for item in problems:
            print(f"FAIL  {item}")
        return 1

    en, fa = read(en_path), read(fa_path)

    if "README.fa.md" not in en:
        problems.append("README.md: no link to README.fa.md (the language switch)")
    if "README.md" not in fa:
        problems.append("README.fa.md: no link back to README.md (the language switch)")

    check_sections("README.md", en, EN_SECTIONS, problems)
    check_sections("README.fa.md", fa, FA_SECTIONS, problems)
    check_mermaid("README.md", en, problems)
    check_mermaid("README.fa.md", fa, problems)

    for label, text in (("README.md", en), ("README.fa.md", fa)):
        for head in headings(text):
            if re.search(r"\bTODO\b|TBD", head):
                problems.append(f"{label}: unfinished heading «{head.strip()}»")

    for path in walk(root):
        if os.path.splitext(path)[1].lower() not in {".md", ".txt", ".py", ".sh", ".yml", ".yaml", ".json", ".php", ".js", ".ts"}:
            continue
        rel = os.path.relpath(path, root)
        if "/templates/" in f"/{rel}":
            continue
        text = read(path)
        if "{{" in text and rel.split(os.sep)[0] in {"README.md", "README.fa.md", "AGENTS.md", "HANDOFF.md", "docs"}:
            problems.append(f"{rel}: unfilled template placeholder («{{{{…}}}}» left in a real doc)")
        for lineno, line in enumerate(text.splitlines(), 1):
            if SECRET_SKIP.search(line):
                continue
            for pattern, kind in SECRETS:
                if pattern.search(line):
                    problems.append(f"{rel}:{lineno}: looks like a {kind}")

    for item in problems:
        print(f"FAIL  {item}")
    if problems:
        print(f"\n{len(problems)} problem(s)")
        return 1

    print("OK    bilingual README, switch links, sections, mermaid, no credential-shaped strings")
    return 0


if __name__ == "__main__":
    sys.exit(main())
