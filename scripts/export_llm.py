#!/usr/bin/env python3
"""
导出全部文档为结构化 JSON，供 LLM 读取。

使用方法:
    python scripts/export_llm.py
"""

import json
import re
from pathlib import Path

DOCS_DIR = Path("docs")
LLM_DIR = Path("docs/llm")

def extract_sections(md_path):
    """从 Markdown 文件中提取标题和内容段落"""
    sections = []
    if not md_path.exists():
        return sections

    text = md_path.read_text(encoding="utf-8")
    # 按 ## 或 ### 标题分割
    chunks = re.split(r'^#{2,3}\s+', text, flags=re.MULTILINE)
    for chunk in chunks[1:]:
        lines = chunk.strip().split('\n')
        title = lines[0].strip()
        content = '\n'.join(lines[1:]).strip()
        content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)
        content = re.sub(r'!\[.*?\]\(.*?\)', '', content)
        content = content.strip()
        if title:
            sections.append({"title": title, "content": content[:500]})
    return sections

def export():
    knowledge = {
        "project": {
            "name": "YizMod QZK",
            "modid": "yizmodqzk",
            "mc_version": "1.21.1",
            "loader": "NeoForge",
            "neo_version": "21.1.228",
            "description": "NeoForge 1.21.1 库模组，为下游模组提供伤害/效果/健康修改框架"
        },
        "api": [],
        "registries": [],
        "knowledge_base": [],
        "pitfalls": [],
        "changelog": []
    }

    # 遍历 docs 下所有 .md 文件
    for md_file in sorted(DOCS_DIR.rglob("*.md")):
        rel = md_file.relative_to(DOCS_DIR)
        sections = extract_sections(md_file)

        path_str = str(rel).replace("\\", "/")
        if path_str == "api/registries.md":
            for s in sections:
                knowledge["registries"].append(s)
        elif path_str.startswith("api/"):
            for s in sections:
                knowledge["api"].append(s)
        elif "pitfalls" in path_str:
            for s in sections:
                knowledge["pitfalls"].append(s)
        elif path_str.startswith("knowledge/"):
            for s in sections:
                knowledge["knowledge_base"].append(s)
        elif path_str.startswith("changelog/"):
            for s in sections:
                knowledge["changelog"].append(s)

    output = LLM_DIR / "knowledge.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(knowledge, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[OK] 已导出 LLM 知识库：{len(knowledge['api'])} API + {len(knowledge['registries'])} 注册表 "
          f"+ {len(knowledge['knowledge_base'])} 知识 + {len(knowledge['pitfalls'])} 踩坑 + {len(knowledge['changelog'])} 变更")

if __name__ == "__main__":
    export()
