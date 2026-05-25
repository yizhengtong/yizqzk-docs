# 会心一击实现复盘

## 时间线

2026-05-26 02:07~04:14, 约 2 小时

## 需求

EntityPerception 天赋, 视线锁定 8 格目标 2.5 秒充能 → 攻击触发突进 + 2 倍真伤 + 等比例改血。

## 遇到的失败 (5 个)

### 1. dispatchContext 缺席

**现象**: 效果不触发, 充能不开始

**根因**: `tizMod.onPlayerTick()` 里 `EffectEventBus.dispatchContext()` 丢了, `AbstractEffect.execute()` 永远不会被调度

**解决**: 补回 `dispatchContext` 调用

### 2. EntityPerception 解锁检查拦截

**现象**: dispatch 跑了但 execute() 还是被跳过

**根因**: dispatch 管道第 2 步 `isUnlocked()` 对所有效果都检查, 包括 ItemPerception。修复成只对 EntityPerception 检查

### 3. getPlayerByUUID 只找玩家

**现象**: `isReady=true timer=50` 但触发消息不出来

**根因**: `player.level().getPlayerByUUID()` 只查在线玩家。假人/怪物是 `LivingEntity` 非 `Player`, 永远返回 null

**解决**: 改用 `((ServerLevel)level).getEntity(UUID)` 查所有实体

### 4. 充能计时器同帧双加

**现象**: 充能不到 2.5 秒就满了

**根因**: `TargetFrameManager.getBest()` 和 `EntityLockRenderer` 各自调一次 `provider.getTarget()`, 每帧 timer +2

**解决**: 用 `level.getGameTime()` 检测同帧重复调用, 跳过第二次

### 5. setNewDamage 走护甲减免

**现象**: 2 倍伤害打不动高护甲/抗性提升

**根因**: `LivingDamageEvent.Pre.setNewDamage()` 修改的值依然经过护甲/附魔管线

**解决**: `event.setNewDamage(0)` 取消原伤害 → 全部改用 `YizModQZKAPI.trueDamage()` 真实伤害 + `EntityASMUtil.modifyHealth()` 直改血绕过护甲

## 架构经验

- **服务端充能** (execute + PlayerDataAPI) 和 **客户端渲染** (Provider + Manager) 是两条独立管线, 必须分别验证
- 实体查找: 用 `ServerLevel.getEntity(UUID)` 而非 `getPlayerByUUID`
- 伤害: `setNewDamage` 不绕护甲, 真伤害用 `YizModQZKAPI.trueDamage()`, 改血用 `EntityASMUtil.modifyHealth()`
- Provider 的 `getTarget()` 可能被多次调用, 内部状态变更需要用帧计数去重

## 最终架构

```
服务端:
  玩家攻击 → LivingDamageEvent.Pre
    → isReady?(PlayerDataAPI timer >= 50) → trueDamage + modifyHealth
  每 tick → dispatchContext → CriticalStrikeEffect.execute()
    → findTarget(8格LOS) → timer++ → EntityLockAPI

客户端:
  每帧 → TargetFrameManager.getBest()
    → CriticalStrikeProvider(prio=10) → 60°锥 + 本地计时
    → EntityLockRenderer 渲染锁定框
```
