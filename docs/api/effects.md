# 效果框架 6 维度

`AbstractEffect` 是效果系统的核心基类，效果 = 6 个维度的组合。

## 6 维度详解

| # | 维度 | 类型 | 说明 |
|---|------|------|------|
| 1 | ID | `ResourceLocation` | 唯一标识 `modid:name` |
| 2 | 父类 (ParentType) | 枚举 5 种 | 残响/铭刻/显化/本形/升灵 |
| 3 | 等级 (Level) | `int` | 效果强度，动态可通过 `getLevel()` 重写 |
| 4 | 感知方式 (PerceptionMode) | OR 集合 | 天赋/词缀/随影/自定义 |
| 5 | 生效条件 (ActivationCondition) | 接口 | 常驻/攻击/投射物命中/自定义 |
| 6 | 稀有度 (Rarity) | 枚举 5 级 | 神话/传说/史诗/精良/平凡 |

## 父类枚举

| 父类 | 英文 | 推荐用途 |
|------|------|---------|
| 残响 | ECHO | 攻击类效果 |
| 铭刻 | INSCRIPTION | 回复类效果 |
| 显化 | MANIFESTATION | 机制类效果 |
| 本形 | ORIGIN | 防御类效果 |
| 升灵 | ASCENSION | 被动类效果 |

## 稀有度枚举

| 稀有度 | 颜色 | 颜色值 |
|--------|------|--------|
| 神话 (MYTHIC) | 红色 | `0xFFFF5555` |
| 传说 (LEGENDARY) | 金色 | `0xFFFFAA00` |
| 史诗 (EPIC) | 紫色 | `0xFFAA00AA` |
| 精良 (RARE) | 蓝色 | `0xFF5555FF` |
| 平凡 (COMMON) | 白色 | `0xFFFFFFFF` |

## 感知方式

| 感知方式 | 绑定 | 说明 |
|---------|------|------|
| EntityPerception | 实体 | 天赋，通过解锁系统管理 |
| ItemPerception | 物品 | 词缀，绑定到物品 |
| ContainerPerception | 容器 | 随影 |
| CustomPerception | — | 自定义 BiPredicate |

## 创建效果

### 代码创建

```java
public class MyEffect extends AbstractEffect {
    public MyEffect() {
        super(
            ResourceLocation.parse("mymod:my_effect"),
            "my_effect",
            "§6我的效果名",
            ParentType.ASCENSION,       // 升灵
            1,                           // 等级
            Set.of(new EntityPerception()),  // 天赋
            new PassiveCondition(),          // 常驻生效
            Rarity.EPIC                      // 史诗
        );
    }

    @Override
    public void execute(EffectContext context) {
        // 效果触发时的逻辑
    }

    @Override
    public int getLevel() {
        // 动态等级（可选重写）
        return levelSupplier.getAsInt();
    }

    @Override
    public String getDisplayName() {
        // 动态显示名（可选重写）
        return "§6效果名 §f[§e等级×" + getLevel() + "§f]";
    }
    
    @Override
    public List<String> getTalentDetailLines(LivingEntity entity) {
        // 天赋面板额外详情行（可选重写）
        return List.of(
            "§8§o意境描述文字",
            "§f100%伤害增幅，50%伤害减免"
        );
    }
}
```

### 注册效果

```java
// 构造函数自动注册，一行即可
YizModQZKAPI.registerEffect(new MyEffect());
```

### 解锁效果

```java
YizModQZKAPI.unlockEffect(player, effectId);
```

### 查询效果

```java
// 获取实体所有已解锁天赋
List<AbstractEffect> talents = YizModQZKAPI.getEntityTalents(player);

// 检查是否解锁
boolean unlocked = YizModQZKAPI.isEffectUnlocked(player, effectId);
```

## 天赋面板展示

所有 `EntityPerception` 类型的效果会自动出现在 `PlayerTalentUI` 中：

```
§6效果名 §f[§e星光×10§f] §fLv.10
  §8└─ 升灵
  §8└─ 生效：常驻生效
  §8└─ 天赋
  §8§o天官赐福，地官赦罪，水官解厄
  §8§o凌空之躯，火德天上，灰烬之神
  §f80%伤害增幅，80%伤害减免，100%回击
  §f10次新生，3点伤害格挡
```
