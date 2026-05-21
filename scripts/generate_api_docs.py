#!/usr/bin/env python3
"""
从 yiz1.21.1 Java 源码扫描，自动生成 API 文档 Markdown。
扫描 src/main/java/net/minecraft/client/yiz/api/ 下的所有 Java 文件。

使用方法:
    python scripts/generate_api_docs.py
"""

import os
import re
import json
from pathlib import Path

YIZ_SRC = Path("D:/ZM/yiz1.21.1/src/main/java")
DOCS_API = Path("D:/ZM/yizqzk-docs/docs/api")

def extract_javadoc_and_signature(filepath):
    """提取 Java 文件中的 Javadoc + 方法签名"""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    methods = []
    # 匹配 Javadoc 注释 + 紧随其后的方法签名
    pattern = re.compile(
        r'(?:/\*\*(.*?)\*/)?\s*'
        r'(?:public\s+)?(?:static\s+)?(?:<\w+>\s+)?'
        r'(\w+(?:<[^>]+>)?)\s+'  # 返回类型
        r'(\w+)\s*'               # 方法名
        r'\(([^)]*)\)'            # 参数列表
        r'\s*(?:throws\s+\w+)?',
        re.DOTALL
    )
    for match in pattern.finditer(content):
        javadoc = match.group(1)
        return_type = match.group(2)
        method_name = match.group(3)
        params = match.group(4)

        # 过滤非公开方法
        lines_before = content[:match.start()].split('\n')
        last_line = lines_before[-1].strip() if lines_before else ""
        if 'private' in last_line and 'public' not in last_line:
            continue

        doc_text = ""
        if javadoc:
            for line in javadoc.split('\n'):
                line = line.strip().strip('*').strip()
                if line and not line.startswith('@'):
                    doc_text += line + " "

        methods.append({
            "name": method_name,
            "return_type": return_type,
            "params": params.strip(),
            "doc": doc_text.strip()
        })
    return methods

def generate_yizmodqzk_api():
    src = YIZ_SRC / "net/minecraft/client/yiz/api"
    all_methods = {}

    for java_file in sorted(src.glob("*.java")):
        classname = java_file.stem
        methods = extract_javadoc_and_signature(java_file)
        if methods:
            all_methods[classname] = methods

    # 生成 Markdown
    lines = [
        "# YizModQZKAPI 完整参考（自动生成）\n",
        "<!-- 此文件由 scripts/generate_api_docs.py 自动生成，请勿手动编辑 -->\n",
    ]

    for classname, methods in sorted(all_methods.items()):
        lines.append(f"\n## {classname}\n")
        lines.append("| 方法 | 返回 | 说明 |")
        lines.append("|------|------|------|")
        for m in methods:
            params_short = m["params"][:60] + "..." if len(m["params"]) > 60 else m["params"]
            signature = f"{m['name']}({params_short})"
            doc = m["doc"][:60] if m["doc"] else "-"
            lines.append(f"| `{signature}` | `{m['return_type']}` | {doc} |")

    (DOCS_API / "yizmodqzk-api.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"[OK] 已生成 API 文档：{len(all_methods)} 个类，{sum(len(v) for v in all_methods.values())} 个方法")

if __name__ == "__main__":
    generate_yizmodqzk_api()
