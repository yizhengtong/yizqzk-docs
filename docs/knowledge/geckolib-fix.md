# GeckoLib 冲突修复记录

## 问题描述

游戏启动时 GeckoLib 报错：

```
Mixin prepare for mod geckolib failed:
MixinTargetAlreadyLoadedException:
  geckolib.mixins.json:common.LivingEntityMixin
  target net.minecraft.world.entity.LivingEntity was loaded too early.
```

游戏在启动阶段崩溃，无法进入主菜单。错误出现在 Mixin 框架的预处理阶段——GeckoLib 的 `LivingEntityMixin` 要求目标类在 Mixin 应用时尚未被加载，但此时 `LivingEntity` 已经被提前加载了。

## 排查过程

### 第一步：定位提前加载的触发点

堆栈跟踪显示 `LivingEntity` 的加载发生在:

```
DisplayWindow.updateModuleReads()
  → Class.forName()
    → ... MixinProcessor.prepareConfigs()
      → MixinTargetAlreadyLoadedException
```

错误发生在 Mixin 框架处理 GeckoLib 的配置时，检测到 `LivingEntity` 已经加载。

### 第二步：排查 CoreMod JS

`yizmodqzk_healban.js` 是 NeoForge CoreMod，在 Mixin 框架初始化之前就会执行类转换。如果 CoreMod 触发了 `LivingEntity` 的加载，GeckoLib 就会失败。

**验证**: 禁用 CoreMod JS 后仍然报错 → CoreMod 只是部分原因。

### 第三步：排查 ASM Agent

`FantasyEndingPlugin.onLoad()` 在 Mixin 配置选择阶段触发 ASM Agent 加载。Agent 注册 `LivingHealthTransformer`，其在类转换管道中可能触发 `LivingEntity` 的提前加载。

**验证**: 将 Agent 引导移到 `tizMod` 构造器后，错误消失。

### 第四步：确定根因

两个因素共同导致：
1. CoreMod JS 在 Mixin 之前就处理 `LivingEntity` 的字节码
2. Agent 在 `FantasyEndingPlugin.onLoad()` 中引导（Mixin 配置选择阶段），触发类加载

修复 CoreMod 但不管 Agent（或反之），问题仍存在。必须同时处理两个。

## 解决方案

### 修改 1：禁用 CoreMod JS

`src/main/resources/META-INF/coremods.json`:
```json
{}
```

CoreMod JS 的功能已被 Mixin + ASM Agent 覆盖，禁用以防意外触发类加载。

### 修改 2：延迟 ASM Agent 引导

`FantasyEndingPlugin.java` — `onLoad()` 不再调用 `AsmBootstrapper.start()`：
```java
@Override
public void onLoad(String mixinPackage) {
    // 不在这里加载 Agent —— 延迟到模组构造器
}
```

`tizMod.java` — 构造器中引导 Agent：
```java
public tizMod(IEventBus modEventBus, ModContainer modContainer) {
    // ... 其他初始化 ...
    
    // 延迟加载 ASM Agent（此时 Mixin 已完成）
    try {
        AsmBootstrapper.start();
    } catch (Exception e) {
        LOGGER.error("Failed to bootstrap ASM Agent", e);
    }
}
```

### 核心原则

任何在 Mixin 框架完成之前触发 `LivingEntity` 类加载的操作都会导致此冲突。需要确保：
1. 不在 Mixin 插件 `onLoad()` 中加载影响实体类的 Agent
2. 不使用 CoreMod 修改实体类（用 Mixin 或普通事件替代）
3. 含有 Minecraft 实体类引用的静态初始化块不会在执行 Mixin 之前触发

## 其他相关冲突

| 模组 | 冲突原因 | 建议 |
|------|---------|------|
| geckolib | LivingEntity 提前加载 | 见本页方案 |
| 其他实体 Mixin 模组 | 同理 | 参考相同排查思路 |
