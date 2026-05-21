# 架构决策记录

## 效果框架 6 维度

**决策**: 效果 = id + parentType + level + perceptionModes(OR) + activationCondition + rarity + execute()

**理由**: 复杂的效果系统拆解为 6 个独立维度，每个维度可独立扩展。下游只需实现 `execute()`，其他维度通过构造函数声明。

## 统一 UI 面板

**决策**: 所有下游模组的汇聚到同一个天赋/词缀面板

**理由**: 类比 JEI 提供统一的物品列表界面，库提供统一的天赋/词缀/随影展示面。下游无需自行实现 UI。通过 `ModRegistries` 注册 + `getTalentDetailLines()` 扩展点实现自定义详情。

## Java Agent 而非纯 Mixin

**决策**: 用 ASM Agent 做字节码改写，Mixin 只做薄层钩子

**理由**: Mixin 在 source 级别工作，无法覆盖所有方法重写路径。ASM Agent 在 class 级别拦截所有子类行为，确保健康修改系统的完整性。

## ASM Agent 引导时机

**决策**: `tizMod` 构造器中引导，而非 `FantasyEndingPlugin.onLoad()`

**理由**: onLoad() 在 Mixin 准备阶段执行，Agent 注册的 ClassFileTransformer 会触发 LivingEntity 提前加载，导致 geckolib 等模组的 MixinTargetAlreadyLoadedException。

## CoreMod JS 禁用

**决策**: `coremods.json` 置空，CoreMod JS 不再加载

**理由**: CoreMod JS 功能已被 Mixin + ASM Agent 覆盖。且 CoreMod 的类转换在时序上更早，更易触发 LivingEntity 提前加载。移除后 GeckoLib 冲突仍需通过 Agent 引导时机解决。

## 数据自动同步

**决策**: `PlayerDataAPI.set()` 自动触发 S2C 同步包

**理由**: 下游模组使用 `PlayerDataAPI.set()` 修改数据时，服务端玩家数据变更但客户端玩家不可见。通过 `SyncPlayerDataPayload` 自动推送到客户端，保证天赋面板等 UI 实时刷新。
