# YizModQZKAPI 完整参考（自动生成）

<!-- 此文件由 scripts/generate_api_docs.py 自动生成，请勿手动编辑 -->


## AttributeBalanceRegistry

| 方法 | 返回 | 说明 |
|------|------|------|
| `enableFor(LivingEntity entity)` | `void` | - |
| `enforceFloors(LivingEntity entity)` | `void` | - |

## ContainerDataStorage

| 方法 | 返回 | 说明 |
|------|------|------|
| `getInstance()` | `ContainerDataStorage` | 容器数据持久化接口 — 将任意 {@link Container} 绑定到世界存档自动存读。 <p>其他模组可通过 {@ |
| `register(String namespace, String key, Container container)` | `AutoCloseable` | 注册一个容器到世界存档自动持久化系统。 |
| `unregister(ResourceLocation id)` | `void` | 注销一个已注册的容器，停止自动存档。 |
| `has(String namespace, String key)` | `boolean` | 判断某个容器是否已注册。 |
| `get(String namespace, String key)` | `Container` | 获取已注册的容器实例。 |
| `saveAll()` | `void` | 立即强制保存所有已注册容器的当前状态到世界存档。 |
| `getDataVersion()` | `int` | 当前数据格式版本号。 版本不匹配时，实现方应自动执行数据迁移而非崩溃。 |
| `setInstance(ContainerDataStorage instance)` | `void` | 由实现方（ChestDataManager）在模组初始化时调用一次。 |

## CounterAttackRegistry

| 方法 | 返回 | 说明 |
|------|------|------|
| `getMultiplier(Player player, LivingEntity source)` | `float` | 回击注册表 <p> 在下游模组注册条件判断，前置模组在受击时触发回击。 通过临时修饰玩家 ATTACK_DAMAGE 实 |
| `register(Trigger trigger)` | `void` | - |
| `tryCounterAttack(Player player, LivingEntity source)` | `void` | 尝试触发回击。 由 Mixin 在 actuallyHurt TAIL 调用。 |
| `AttributeModifier(MODIFIER_ID, (double)` | `new` | - |
| `attack()` | `确保` | - |

## DamageAttributeRegistry

| 方法 | 返回 | 说明 |
|------|------|------|
| `register(Holder<Attribute> holder)` | `void` | 伤害属性注册表 <p> 注册的属性将作为额外伤害源。攻击者每次近战攻击时， 自动计算所有已注册属性的加权总和，通过 {@ |
| `register(Holder<Attribute> holder, float scale)` | `void` | 注册一个属性为伤害属性，并指定比例系数。 攻击者拥有该属性时，每次攻击额外附加 {@code value * scale |
| `getTotalValue(LivingEntity attacker)` | `float` | 获取攻击者身上所有已注册伤害属性的加权总值。 |

## DamageEvent

| 方法 | 返回 | 说明 |
|------|------|------|
| `cancel(String reason)` | `void` | 伤害应用事件（通知入口） <p> 在 {@link YizModQZKAPI#damage} 或 {@link YizM |
| `isCanceled()` | `boolean` | - |
| `getTarget()` | `LivingEntity` | 伤害承受方 |
| `getAmount()` | `float` | 伤害数值（可修改） |
| `setAmount(float amount)` | `void` | 修改伤害数值 |
| `getType()` | `DamageType` | 伤害类型 |
| `getSource()` | `Entity` | 伤害来源（攻击者），可能为空 |
| `getCancelReason()` | `String` | 取消原因 |

## DamageReductionRegistry

| 方法 | 返回 | 说明 |
|------|------|------|
| `markReductionApplied()` | `void` | 伤害减免注册表（Agent 级写前钩子） <p> 由 ASM Agent 在 {@code LivingEntity.s |
| `consumeReductionApplied()` | `boolean` | Mixin 层调用：检查 Agent 层是否已处理减免。 |
| `modify(LivingEntity entity, float oldHealth, float newHealth)` | `float` | 健康值修改器，在 setHealth() 最终写入前执行 / public interface HealthModifi |
| `register(HealthModifier modifier)` | `void` | 注册一个健康值修改器 |
| `applyBeforeSetHealth(LivingEntity entity, float newHealth)` | `float` | 由 ASM Agent 在 setHealth(float) 入口调用 |

## DamageResult

| 方法 | 返回 | 说明 |
|------|------|------|
| `DamageResult(float applied,
    float delta,
    boolean canceled,
    St...)` | `record` | 伤害应用结果 |
| `success(float applied, float delta)` | `DamageResult` | - |
| `DamageResult(applied, delta, false, "")` | `new` | - |
| `canceled(String reason)` | `DamageResult` | - |
| `DamageResult(0, 0, true, reason)` | `new` | - |

## FlightAbilityRegistry

| 方法 | 返回 | 说明 |
|------|------|------|
| `mayFly()` | `强制` | - |
| `shouldHaveFlight(LivingEntity entity)` | `boolean` | - |
| `register(Condition condition)` | `void` | - |
| `shouldHaveFlight(LivingEntity entity)` | `boolean` | - |

## FlightOptimizationRegistry

| 方法 | 返回 | 说明 |
|------|------|------|
| `shouldOptimize(LivingEntity entity)` | `boolean` | - |
| `register(Condition condition)` | `void` | - |
| `shouldOptimize(LivingEntity entity)` | `boolean` | - |

## HealBanAttributeRegistry

| 方法 | 返回 | 说明 |
|------|------|------|
| `registerPercent(Holder<Attribute> holder, float scale)` | `void` | 禁疗属性注册表 <p> 注册的属性将自动作为禁疗源。攻击者每次近战攻击时， 自动计算所有已注册属性的总和，为目标施加禁疗 |
| `registerFixed(Holder<Attribute> holder, float scale)` | `void` | 注册一个属性为固定值禁疗属性。 <p> 攻击者每拥有 1 点该属性，目标每次治疗被削减 {@code scale} 点。 |
| `getPercentTotal(LivingEntity attacker)` | `float` | 获取攻击者身上所有已注册百分比禁疗属性的总值（已乘缩放系数）。 |
| `getFixedTotal(LivingEntity attacker)` | `float` | 获取攻击者身上所有已注册固定值禁疗属性的总值（已乘缩放系数）。 |

## KnockbackImmunityRegistry

| 方法 | 返回 | 说明 |
|------|------|------|
| `isImmune(LivingEntity entity)` | `boolean` | - |
| `register(Condition condition)` | `void` | - |
| `isImmune(LivingEntity entity)` | `boolean` | - |

## NoCollisionRegistry

| 方法 | 返回 | 说明 |
|------|------|------|
| `isImmune(LivingEntity entity)` | `boolean` | - |
| `register(Condition condition)` | `void` | - |
| `isImmune(LivingEntity entity)` | `boolean` | - |

## PlayerDataAPI

| 方法 | 返回 | 说明 |
|------|------|------|
| `setSyncCallback(java.util.function.BiConsumer<Player, String> callback)` | `void` | 通用玩家数据附件 API <p> 为下游模组提供类型安全的玩家数据存储，自动持久化。 所有数据默认持久化到玩家 NBT  |
| `register(String key, Codec<T> codec, T defaultValue)` | `void` | 注册一个玩家数据条目。 |
| `IllegalArgumentException("Unknown PlayerData key: " + key)` | `new` | - |
| `set(Player player, String key, T value)` | `void` | 获取玩家指定键的数据，不存在时返回默认值。 / public static <T> T get(Player playe |
| `discard(Player player, String key)` | `void` | 丢弃指定键的数据：从 NBT 中移除，下次存档不再保存， {@link #get} 将返回默认值。 |
| `discardAll(Player player)` | `void` | 丢弃该玩家所有已注册键的数据，完全重置为默认状态。 |
| `CompoundTag()` | `new` | - |
| `CompoundTag()` | `new` | - |
| `CompoundTag()` | `new` | - |

## ProjectileImmunityRegistry

| 方法 | 返回 | 说明 |
|------|------|------|
| `hurt()` | `前置在` | - |
| `isImmune(LivingEntity entity)` | `boolean` | - |
| `register(Condition condition)` | `void` | - |
| `isImmune(LivingEntity entity)` | `boolean` | - |

## ProjectileReflectionSystem

| 方法 | 返回 | 说明 |
|------|------|------|
| `tick(Player player)` | `void` | 投射物返还系统 <p> 下游注册反射条件，前置自动检测范围内的投射物并处理： 无主人 → 移除，有主人 → 转移所有权并 |

## ShaderEnvironmentAPI

| 方法 | 返回 | 说明 |
|------|------|------|
| `isIrisLoaded()` | `boolean` | 着色器环境检测与兼容性 API — 着色器保护 <p>提供 Iris/Oculus 光影模组的检测和兼容性配置， 确保自 |
| `isShaderPackInUse()` | `boolean` | 检测当前是否启用了光影包（Iris shader pack）。 <p>优先使用 Iris 内部快速路径 {@code I |
| `isUnknownShaderAllowed()` | `boolean` | 查询 Iris 是否允许未知着色器。 <p>返回 {@link net.irisshaders.iris.config. |
| `setAllowUnknownShaders(boolean allow)` | `void` | 设置 Iris 是否允许未知着色器。 <p>当启用时，自定义 {@code ShaderInstance} 可在光影包激 |
| `ensureShaderCompatibility()` | `boolean` | 确保自定义着色器兼容性 — 自动启用 allowUnknownShaders。 <p>在注册自定义着色器之前调用此方法， |
| `isUnknownShaderAllowed()` | `return` | - |

## ShaderManager

| 方法 | 返回 | 说明 |
|------|------|------|
| `registerPreset(String name, ShaderDescriptor desc)` | `void` | 中央着色器管理器 — 管理多个着色器预设 (A/B/C/D) 并可运行时切换。 <p>每个 {@link ShaderP |
| `ShaderPreset(name, desc)` | `new` | - |
| `setActivePreset(String name)` | `void` | 切换当前激活的预设 |
| `getActivePresetName()` | `String` | 获取当前激活的预设名 |
| `registerItemPredicate(Predicate<ItemStack> predicate)` | `void` | 注册物品谓词 |
| `registerArmorPredicate(Predicate<ItemStack> predicate)` | `void` | 注册盔甲谓词 |
| `setCosmicUVs(float[] uvs)` | `void` | 设置 cosmic 图标 UV |
| `applyCosmicUVs(ShaderInstance shader)` | `void` | 将 UV 写入着色器的 cosmicuvs uniform（供 Mixin 调用） |
| `hasItemEffect(ItemStack stack)` | `boolean` | 判断物品是否应用着色器效果 |
| `hasArmorEffect(ItemStack stack)` | `boolean` | 判断盔甲是否应用着色器效果 |
| `getItemRenderType()` | `RenderType` | 获取当前激活预设的物品 RenderType |
| `IllegalStateException("No active shader preset")` | `new` | - |
| `getItemGuiRenderType()` | `RenderType` | 获取当前激活预设的 GUI RenderType |
| `IllegalStateException("No active shader preset")` | `new` | - |
| `getItemDirectRenderType()` | `RenderType` | 获取当前激活预设的第一人称 RenderType |
| `IllegalStateException("No active shader preset")` | `new` | - |
| `getItemEntityRenderType()` | `RenderType` | 获取当前激活预设的实体 RenderType |
| `IllegalStateException("No active shader preset")` | `new` | - |
| `getArmorRenderType()` | `RenderType` | 获取当前激活预设的盔甲 RenderType |
| `IllegalStateException("No active shader preset")` | `new` | - |
| `getActiveItemShader()` | `ShaderInstance` | 获取当前激活预设的物品着色器 |
| `getActiveArmorShader()` | `ShaderInstance` | 获取当前激活预设的盔甲着色器 |
| `onRegisterShaders(RegisterShadersEvent event)` | `void` | - |
| `ShaderInstance(event.getResourceProvider()` | `new` | - |
| `ShaderInstance(event.getResourceProvider()` | `new` | - |
| `ShaderStateShard(()` | `new` | - |
| `TextureStateShard(TextureAtlas.LOCATION_BLOCKS, false, false)` | `new` | - |
| `ShaderStateShard(()` | `new` | - |
| `getArmorStarOverlayType()` | `RenderType` | 为非 z 系列 TAIL 叠加创建 RenderType。使用 EQUAL 深度测试， 确保星空只渲染在原版盔甲已写入深 |
| `ShaderStateShard(()` | `new` | - |
| `TextureStateShard(TextureAtlas.LOCATION_BLOCKS, false, false)` | `new` | - |
| `create("shader_" + preset.name + "_armor_overlay",
                ...)` | `return` | - |
| `TransparencyStateShard("film_trans",
                ()` | `new` | - |
| `DepthTestStateShard("<=", 515)` | `new` | - |
| `ShaderDescriptor(String namespace,           // modid
            String item...)` | `record` | 着色器预设描述符（下游模组注册时传入） |

## ShaderProtectionRegistry

| 方法 | 返回 | 说明 |
|------|------|------|
| `registerShader(ResourceLocation id, VertexFormat vertexFormat)` | `void` | 着色器注册保护注册表 — 受 Iris 保护的着色器注册中心 <p>下游模组通过此注册表提交需要 Iris 光影兼容保护 |
| `IllegalArgumentException("Shader id must not be null")` | `new` | - |
| `IllegalArgumentException("VertexFormat must not be null")` | `new` | - |
| `for(ShaderEntry entry : ENTRIES)` | `避免重复注册` | - |
| `ShaderEntry(id, vertexFormat)` | `new` | - |
| `getShader(ResourceLocation id)` | `ShaderInstance` | 获取已注册并加载完成的 {@link ShaderInstance}。 <p>必须在 {@link RegisterSh |
| `getAllEntries()` | `List<ShaderEntry>` | 获取所有已注册的着色器条目（只读快照）。 |
| `isShaderLoaded(ResourceLocation id)` | `boolean` | 检查指定着色器是否已成功加载。 |
| `onRegisterShaders(RegisterShadersEvent event)` | `void` | 处理 {@link RegisterShadersEvent}— 自动注册所有受保护的着色器。 <p>在前置库客户端初始 |
| `if(ShaderEnvironmentAPI.isIrisLoaded()` | `else` | - |
| `ensured(allowUnknownShaders={})` | `compatibility` | - |
| `for(ShaderEntry entry : ENTRIES)` | `批量注册着色器` | - |
| `ShaderInstance(event.getResourceProvider()` | `new` | - |
| `ShaderEntry(ResourceLocation id, VertexFormat vertexFormat)` | `record` | 着色器注册条目。 |
| `IllegalArgumentException("id must not be null")` | `new` | - |
| `IllegalArgumentException("vertexFormat must not be null")` | `new` | - |

## SpecialDamageAttributeRegistry

| 方法 | 返回 | 说明 |
|------|------|------|
| `registerTrueDamage(Holder<Attribute> holder, float scale)` | `void` | 特殊伤害属性注册表 <p> 注册的属性将自动作为真实伤害/破甲伤害/破无敌帧的数值来源。 攻击者每次近战攻击时，自动计算 |
| `registerArmorPiercing(Holder<Attribute> holder, float scale)` | `void` | 注册一个属性为破甲伤害属性。 <p> 攻击者每拥有 1 点该属性，每次近战攻击附加 {@code scale} 点破甲伤 |
| `registerPierceInvulnerability(Holder<Attribute> holder, float scale)` | `void` | 注册一个属性为破无敌帧属性。 <p> 攻击者拥有该属性时（总值 > 0），破甲伤害同时无视无敌帧。 单独注册该属性但不注 |
| `getTrueDamageTotal(LivingEntity attacker)` | `float` | 获取攻击者身上所有已注册真实伤害属性的总值（已乘缩放系数）。 |
| `getArmorPiercingTotal(LivingEntity attacker)` | `float` | 获取攻击者身上所有已注册破甲伤害属性的总值（已乘缩放系数）。 |
| `hasPierceInvulnerability(LivingEntity attacker)` | `boolean` | 检查攻击者是否拥有破无敌帧属性（总值 > 0）。 |

## StarShaderRegistry

| 方法 | 返回 | 说明 |
|------|------|------|
| `registerStarItem(Predicate<ItemStack> predicate)` | `void` | 星空着色器注册表 — 着色器渲染对接 API（A层→B层桥梁） <p>前置库提供星空着色器渲染能力，下游模组通过此 AP |
| `IllegalArgumentException("predicate must not be null")` | `new` | - |
| `registered(total: {})` | `predicate` | - |
| `registerStarArmor(Predicate<ItemStack> predicate)` | `void` | 注册一个盔甲谓词：匹配的盔甲在实体上渲染时叠加星空效果。 |
| `IllegalArgumentException("predicate must not be null")` | `new` | - |
| `registered(total: {})` | `predicate` | - |
| `hasStarEffect(ItemStack stack)` | `boolean` | 供 Mixin 判断物品是否需要星空叠加。 |
| `hasStarArmorEffect(ItemStack stack)` | `boolean` | 供 Mixin 判断盔甲是否需要星空叠加。 |
| `getStarArmorShader()` | `ShaderInstance` | - |
| `starGlint()` | `RenderType` | - |
| `IllegalStateException("Star shader not yet registered")` | `new` | - |
| `starGlintDirect()` | `RenderType` | - |
| `IllegalStateException("Star shader not yet registered")` | `new` | - |
| `starEntityGlint()` | `RenderType` | - |
| `IllegalStateException("Star shader not yet registered")` | `new` | - |
| `starArmorGlint()` | `RenderType` | - |
| `IllegalStateException("Star shader not yet registered")` | `new` | - |
| `onRegisterShaders(RegisterShadersEvent event)` | `void` | SRC_COLOR + ONE 叠加混合 → 原色变亮，暗色叠加星辉 */ private static final T |
| `ShaderInstance(event.getResourceProvider()` | `new` | - |
| `ShaderInstance(event.getResourceProvider()` | `new` | - |
| `TextureStateShard(TextureAtlas.LOCATION_BLOCKS, false, false)` | `new` | - |

## UndyingRegistry

| 方法 | 返回 | 说明 |
|------|------|------|
| `tryRevive(LivingEntity entity, DamageSource source)` | `float` | 复活系统注册表，挂接原版不死图腾路径 {@code checkTotemDeathProtection}。 自定义复活动 |
| `if(!result.displayItem()` | `读取并替换` | - |

## YizModQZKAPI

| 方法 | 返回 | 说明 |
|------|------|------|
| `damage(LivingEntity target, float amount, Entity source)` | `DamageResult` | YizMod QZK 公开 API <p> 第三方模组通过此接口与前置库交互。 伤害相关方法会触发 {@link Dam |
| `DamageEvent(target, amount, DamageType.FLAT, source)` | `new` | - |
| `if(event.isCanceled()` | `检查取消` | - |
| `percentDamage(LivingEntity target, float percent, Entity source)` | `DamageResult` | 通知入口②：对目标造成最大生命值百分比伤害。 <p> 计算方式：amount = target.getMaxHealth |
| `DamageEvent(target, amount, DamageType.PERCENT, source)` | `new` | - |
| `if(event.isCanceled()` | `检查取消` | - |
| `trueDamage(LivingEntity target, float amount, Entity source)` | `DamageResult` | 真实伤害：直接扣除目标生命值，无视护甲、无敌帧、伤害减免。 <p> 伤害值发布 {@link DamageEvent}， |
| `DamageEvent(target, amount, DamageType.TRUE, source)` | `new` | - |
| `armorPiercingDamage(LivingEntity target, float amount, Entity source)` | `DamageResult` | 破甲伤害：跳过护甲减伤，仍受无敌帧限制。 <p> 使用 {@link DamageSource#magic()} 作为伤 |
| `DamageEvent(target, amount, DamageType.ARMOR_PIERCING, source)` | `new` | - |
| `pierceInvulnerabilityDamage(LivingEntity target, float amount, Entity source)` | `DamageResult` | 破无敌帧伤害：无视目标无敌帧，但仍经过护甲减伤。 <p> 临时清除目标 {@code invulnerableTime} |
| `DamageEvent(target, amount, DamageType.PIERCE_INVULNERABILITY, source)` | `new` | - |
| `armorPiercingAndPierceInvulnerabilityDamage(LivingEntity target, float amount, Entity source)` | `DamageResult` | 破甲 + 破无敌帧：跳过护甲且无视无敌帧。 |
| `DamageEvent(target, amount, DamageType.ARMOR_PIERCING, source)` | `new` | - |
| `registerTrueDamageAttribute(Holder<Attribute> holder, float scale)` | `void` | 注册一个属性为真实伤害属性。 <p> 攻击者拥有该属性时，每次近战攻击额外附加等量真实伤害。 真实伤害直接 {@code |
| `registerArmorPiercingAttribute(Holder<Attribute> holder, float scale)` | `void` | 注册一个属性为破甲伤害属性。 <p> 攻击者拥有该属性时，每次近战攻击附加等量破甲伤害。 破甲伤害跳过护甲减伤。 </p |
| `registerPierceInvulnerabilityAttribute(Holder<Attribute> holder, float scale)` | `void` | 注册一个属性为破无敌帧属性。 <p> 攻击者拥有该属性时（总值 > 0），破甲伤害同时无视目标无敌帧。 </p> |
| `registerDamageAttribute(Holder<Attribute> holder)` | `void` | 注册一个属性为伤害属性。 <p> 攻击者拥有该属性时，每次近战攻击额外附加等量伤害。 伤害经由三層系统（Delta →  |
| `getDamageAttributeValue(LivingEntity attacker)` | `float` | 获取攻击者身上所有已注册伤害属性的总值。 |
| `modifyHealth(LivingEntity target, float delta)` | `void` | 直接增减实体健康值（治疗或伤害）。 <p> 正数 = 治疗，负数 = 伤害。<br> 经过三層系统修改所有 Float  |
| `setHealth(LivingEntity target, float health)` | `void` | 直接设置实体健康值（绝对值）。 <p> 与 {@link #modifyHealth} 一样绕过 {@code hurt |
| `setDamageEffectsEnabled(boolean enabled)` | `void` | 设置 Delta 改血系统是否触发受伤动画和音效。 <p> 开启后，通过 {@link #damage} / {@lin |
| `isDamageEffectsEnabled()` | `boolean` | 查询 Delta 伤害效果开关状态。 |
| `setHealBan(LivingEntity entity, float percent, float fixedAmount)` | `void` | 从健康值根本禁止治疗（百分比 + 固定值）。 <p> 在 {@code modifyHealth} 和 {@code H |
| `setHealBanPercent(LivingEntity entity, float percent)` | `void` | 百分比禁疗（子方法①）。 <p> 按百分比削减所有治疗量。 例：percent=50 → 所有治疗仅生效一半。 </p> |
| `setHealBanFixed(LivingEntity entity, float fixedAmount)` | `void` | 固定值禁疗（子方法②）。 <p> 每次治疗减掉固定数值。治疗量不足时完全取消。 例：fixedAmount=10 → 1 |
| `registerHealBanPercentAttribute(Holder<Attribute> holder, float scale)` | `void` | 注册一个属性为百分比禁疗属性。 <p> 攻击者拥有该属性时，每次攻击为目标施加百分比禁疗。 例：registerHeal |
| `registerHealBanFixedAttribute(Holder<Attribute> holder, float scale)` | `void` | 注册一个属性为固定值禁疗属性。 <p> 攻击者拥有该属性时，每次攻击为目标施加固定值禁疗。 例：registerHeal |
| `registerEffect(AbstractEffect effect)` | `void` | 注册效果。 |
| `getEffect(ResourceLocation id)` | `Optional<AbstractEffect>` | 根据 ID 获取效果。 |
| `unlockEffect(LivingEntity entity, ResourceLocation effectId)` | `void` | 为实体解锁效果。 服务端调用后自动同步到客户端。 |
| `isEffectUnlocked(LivingEntity entity, ResourceLocation effectId)` | `boolean` | 检查实体是否已解锁效果。 |
| `dispatchContext(EffectContext context)` | `void` | 分发效果上下文（触发效果系统）。 |
| `getAllEffects()` | `List<AbstractEffect>` | 获取所有注册的效果。 |
| `getEntityTalents(LivingEntity entity)` | `List<AbstractEffect>` | 获取实体所有已解锁的天赋。 <p> 自动过滤出 {@link net.minecraft.client.yiz.effe |
| `refreshUI()` | `void` | 请求刷新所有 YizMod QZK UI 组件。 <p> 下游模组在解锁新天赋、变更效果或需要重新渲染 UI 时调用此方 |
| `getAttackDamage(ItemStack stack)` | `double` | - |
| `setAttackDamage(ItemStack stack, double value)` | `void` | - |
| `addAttackDamage(ItemStack stack, double delta)` | `void` | - |
| `getAttackSpeed(ItemStack stack)` | `double` | - |
| `setAttackSpeed(ItemStack stack, double value)` | `void` | - |
| `addAttackSpeed(ItemStack stack, double delta)` | `void` | - |
| `getInteractionRange(ItemStack stack)` | `double` | - |
| `setInteractionRange(ItemStack stack, double value)` | `void` | - |
| `addInteractionRange(ItemStack stack, double delta)` | `void` | - |
| `getSweepRatio(ItemStack stack)` | `double` | - |
| `setSweepRatio(ItemStack stack, double value)` | `void` | - |
| `addSweepRatio(ItemStack stack, double delta)` | `void` | - |
| `isSweepDecayEnabled(ItemStack stack)` | `boolean` | - |
| `setSweepDecay(ItemStack stack, boolean enabled)` | `void` | - |
| `getMaxDurability(ItemStack stack)` | `int` | - |
| `setMaxDurability(ItemStack stack, int value)` | `void` | - |
| `addMaxDurability(ItemStack stack, int delta)` | `void` | - |
| `getDamageAmplification(ItemStack stack)` | `double` | - |
| `setDamageAmplification(ItemStack stack, double percent)` | `void` | - |
| `addDamageAmplification(ItemStack stack, double delta)` | `void` | - |
| `getDamageReduction(ItemStack stack)` | `double` | - |
| `setDamageReduction(ItemStack stack, double percent)` | `void` | - |
| `addDamageReduction(ItemStack stack, double delta)` | `void` | - |
| `registerCommand(com.mojang.brigadier.builder.LiteralArgumentBuilder<net.mine...)` | `void` | 注册一个指令（完整 builder）。 <pre>{@code YizModQZKAPI.registerCommand |
| `registerSimpleCommand(String name, com.mojang.brigadier.Command<net.minecraft.comm...)` | `void` | 快捷注册：无参数的字面指令。 <pre>{@code YizModQZKAPI.registerSimpleComman |
| `cleanupAttackTarget(net.minecraft.world.entity.player.Player player)` | `void` | 获取玩家最近一次攻击的原始目标。 <p>由 ASM Agent 在 {@code Player.attack()} 最早 |
| `enableProtection(net.minecraft.world.entity.player.Player player)` | `boolean` | 启用玩家保护态（Unsafe class 指针替换）。 保护态下玩家免疫一切伤害，生命值恒 ≥ 0.5。 |
| `disableProtection(net.minecraft.world.entity.player.Player player)` | `boolean` | 关闭玩家保护态，恢复原始类。 |
| `isProtected(net.minecraft.world.entity.player.Player player)` | `boolean` | 查询玩家是否处于保护态。 |
| `attachEffectToItem(ItemStack stack, AbstractEffect effect)` | `void` | 直接为物品附加效果（写入 NBT）。 |
| `getItemEffects(ItemStack stack)` | `List<AbstractEffect>` | 获取物品上的所有效果。 |