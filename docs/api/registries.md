# 注册表 API 参考

全部位于 `net.minecraft.client.yiz.api` 包，都是静态方法，下游在模组构造器中调用。

## PlayerDataAPI

类型安全的玩家数据持久化键值存储，基于 NeoForge `AttachmentType`。

```java
// 注册数据类型（在模组构造器中）
PlayerDataAPI.register("mymod:star_level", Codec.intRange(0, 10), 0);
PlayerDataAPI.register("mymod:has_star_body", Codec.BOOL, false);

// 读写
int level = PlayerDataAPI.get(player, "mymod:star_level");
PlayerDataAPI.set(player, "mymod:star_level", 5);

// 丢弃
PlayerDataAPI.discard(player, "mymod:star_level");
PlayerDataAPI.discardAll(player);
```

!!! important "自动同步"
    `set()` 每次写入时自动触发 `SyncPlayerDataPayload` 网络包从服务端推送到客户端，下游无需手动同步。

## DamageReductionRegistry

伤害减免钩子，在 `setHealth()` 最终写入前拦截修改。

```java
DamageReductionRegistry.register((entity, oldHealth, newHealth) -> {
    // entity: 受伤实体
    // oldHealth: setHealth 前的血量
    // newHealth: setHealth 传入的原始值
    return newHealth * 0.5f; // 50% 减免
});
```

## CounterAttackRegistry

回击触发条件，命中时反弹伤害给攻击者。

```java
CounterAttackRegistry.register((player, source) -> {
    // player: 被攻击的玩家
    // source: 伤害来源
    // 返回 true 触发回击
    return true;
});
```

## UndyingRegistry

自定义复活，类似不死图腾。

```java
UndyingRegistry.register((entity, source) -> {
    // 返回 true 触发复活
    // 需要自行在回调中处理：消耗复活道具、设置血量等
    return StarDataHelper.canConsumeLayer(player);
});
```

## ProjectileReflectionSystem

投射物返还，命中时反弹回攻击者。

```java
ProjectileReflectionSystem.register(entity -> {
    return entity instanceof Player;
});
```

## ProjectileImmunityRegistry

投射物免疫。

```java
ProjectileImmunityRegistry.register(entity -> {
    return StarDataHelper.getStarLevel(entity) > 0;
});
```

## NoCollisionRegistry

碰撞免疫（推进和碰撞检测）。

```java
NoCollisionRegistry.register(entity -> {
    return StarDataHelper.getStarLevel(entity) > 0;
});
```

## KnockbackImmunityRegistry

击退霸体。

```java
KnockbackImmunityRegistry.register(entity -> {
    return StarDataHelper.getStarLevel(entity) > 0;
});
```

## FlightOptimizationRegistry

飞行惯性优化条件。

```java
FlightOptimizationRegistry.register(entity -> {
    return true; // 启用飞行惯性优化
});
```

## FlightAbilityRegistry

绝对飞行权。

```java
FlightAbilityRegistry.register(entity -> {
    return true; // 强制允许飞行
});
```

## DamageAttributeRegistry

把属性值转为额外伤害（乘以缩放系数）。

```java
// 把攻击力属性绑定为额外伤害，缩放系数 0.08（每级 8%）
DamageAttributeRegistry.register(Attributes.ATTACK_DAMAGE, 0.08f);
```

## AttributeBalanceRegistry

属性正负锁定，每 tick 恢复属性底线。

```java
AttributeBalanceRegistry.enableFor(player);
```
