# API 参考

YizMod QZK 的公开 API 全部位于包 `net.minecraft.client.yiz.api` 下，通过 `YizModQZKAPI` 和其他静态注册表类提供给下游模组使用。

## 结构概览

| 模块 | 入口类 | 说明 |
|------|--------|------|
| 效果框架 | `YizModQZKAPI` | 效果注册、解锁、查询、事件分发 |
| 注册表 API | 各 `*Registry` 类 | 伤害减免、回击、飞行等能力的条件注册 |
| 玩家数据 | `PlayerDataAPI` | 类型安全的玩家数据持久化键值存储 |

## 目录

- [YizModQZKAPI 完整参考](yizmodqzk-api.md) — 所有公开方法签名与说明
- [注册表 API 参考](registries.md) — 全部 12 个注册表的使用方式
- [效果框架 6 维度](effects.md) — AbstractEffect 详解

!!! tip "自动生成"
    API 文档由脚本从 Java 源码自动生成，确保与实际代码保持一致。
