# YizMod QZK 文档站

欢迎来到 YizMod QZK 文档站。这里汇集了模组的完整 API 参考、架构设计决策、开发踩坑记录和最新变更信息。

## 关于 YizMod QZK

YizMod QZK 是一个 **NeoForge 1.21.1 库模组 (Library Mod)**，MODID=``yizmodqzk``，为下游模组提供伤害/效果/健康修改框架。

- **包名**: ``net.minecraft.client.yiz``
- **模组 ID**: ``yizmodqzk``
- **NeoForge 版本**: 21.1.228+
- **MC 版本**: 1.21.1
- **Java 版本**: 21

## 快速导航

| 章节 | 内容 |
|------|------|
| [📖 API 参考](api/index.md) | YizModQZKAPI 全方法签名、注册表 API、效果框架 |
| [🧠 知识库](knowledge/index.md) | 架构决策、踩坑记录、GeckoLib 冲突修复 |
| [📝 变更日志](changelog/index.md) | 基于 Git 历史自动生成的最新变更 |
| [🤖 AI 知识库](llm/index.md) | 供大语言模型读取的结构化知识库 |

## 下游模组快速开始

```groovy
// build.gradle
repositories {
    maven { url = 'file:///path/to/yiz1.21.1/repo' }
}
dependencies {
    implementation "net.minecraft.client.yiz:yizmodqzk:1.0.0"
}
```

```java
// 注册数据和效果
PlayerDataAPI.register("mymod:my_data", Codec.INT, 0);
YizModQZKAPI.registerEffect(new MyEffect());

// 注册能力
DamageReductionRegistry.register((entity, oldHealth, newHealth) -> {
    // 返回修改后的 health 值
    return newHealth * 0.5f; // 50% 伤害减免
});

// 注册指令
YizModQZKAPI.registerSimpleCommand("mycmd", ctx -> {
    ctx.getSource().sendSuccess(() -> Component.literal("Hello!"), true);
});
```

## 项目相关

- [GitHub 仓库](https://github.com/yizhengtong/yiz-qzk)
- [下游模组模板](https://github.com/yizhengtong/yizxgmod-template-1.21.1)
