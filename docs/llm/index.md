# AI 知识库

此目录包含供大语言模型（LLM）读取的结构化知识库数据。

## 文件说明

| 文件 | 格式 | 内容 |
|------|------|------|
| `knowledge.json` | JSON | 全部文档的结构化导出，包含 API 签名、架构决策、踩坑记录 |

## 生成方式

```bash
python scripts/export_llm.py
```

## AI 使用指引

将 `knowledge.json` 文件内容作为上下文提供给 LLM，即可获得关于 YizMod QZK 的全部知识。

### 数据格式

```json
{
  "project": {
    "name": "YizMod QZK",
    "modid": "yizmodqzk",
    "mc_version": "1.21.1",
    "loader": "NeoForge",
    "neo_version": "21.1.228"
  },
  "api": [
    {
      "name": "YizModQZKAPI.damage",
      "signature": "damage(LivingEntity, float, Entity) -> DamageResult",
      "description": "固定数值伤害（Delta 系统）"
    }
  ],
  "registries": [
    {
      "name": "DamageReductionRegistry",
      "method": "register(BiFunction)",
      "description": "伤害减免钩子"
    }
  ],
  "knowledge_base": [
    {
      "title": "GeckoLib 冲突修复",
      "content": "..."
    }
  ],
  "pitfalls": [
    {
      "title": "...",
      "cause": "...",
      "fix": "..."
    }
  ]
}
```
