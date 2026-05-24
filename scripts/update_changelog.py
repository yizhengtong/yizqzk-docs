#!/usr/bin/env python3
"""
从 Git 历史生成变更日志 Markdown。

使用方法:
    python scripts/update_changelog.py
"""

import subprocess
import os
from pathlib import Path
from datetime import datetime

DOCS_CHANGELOG = Path("/mnt/d/ZM/yizgzq/yizqzk-docs/docs/changelog/index.md")
REPO_PATH = "/mnt/d/ZM/yizgzq/yiz1.21.1"

def run_git_log():
    os.chdir(REPO_PATH)
    result = subprocess.run(
        ["git", "log", "--oneline", "--no-decorate", "-50"],
        capture_output=True, text=True, encoding="utf-8"
    )
    return result.stdout.strip().split("\n")

def run_git_show(hash):
    """获取某个 commit 的详细信息"""
    os.chdir(REPO_PATH)
    result = subprocess.run(
        ["git", "log", "-1", "--format=%H|%ai|%s", hash],
        capture_output=True, text=True, encoding="utf-8"
    )
    parts = result.stdout.strip().split("|", 2)
    return {
        "hash": parts[0][:8] if len(parts) > 0 else hash[:8],
        "date": parts[1] if len(parts) > 1 else "",
        "subject": parts[2] if len(parts) > 2 else ""
    }

def generate():
    commits = run_git_log()
    lines = [
        "# 变更日志\n",
        f"最后更新: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n",
        f"来源仓库: `{REPO_PATH}`\n",
        "---\n"
    ]

    for commit_line in commits:
        if not commit_line.strip():
            continue
        hash_part = commit_line.split()[0]
        detail = run_git_show(hash_part)
        date_str = detail["date"][:10] if detail["date"] else "unknown"
        lines.append(f"### {date_str} — `{detail['hash']}`")
        lines.append(f"\n{detail['subject']}\n")

    DOCS_CHANGELOG.parent.mkdir(parents=True, exist_ok=True)
    DOCS_CHANGELOG.write_text("\n".join(lines), encoding="utf-8")
    print(f"[OK] 已生成变更日志：{len(commits)} 条")

if __name__ == "__main__":
    generate()
