# 踩坑集

## GeckoLib MixinTargetAlreadyLoadedException

**现象**: 游戏启动时 GeckoLib 报 `MixinTargetAlreadyLoadedException: target LivingEntity was loaded too early`，游戏崩溃。

**原因**: 两个触发源：
1. CoreMod JS (`yizmodqzk_healban.js`) — 在 Mixin 预处理之前就转换了 `LivingEntity` 的字节码
2. `FantasyEndingPlugin.onLoad()` 加载 ASM Agent — Agent 注册的 `ClassFileTransformer` 在 Mixin 准备阶段触发了 `LivingEntity` 的加载

**修复**: 
- 禁用 CoreMod JS（`coremods.json` 置空）
- Agent 引导移到 `tizMod` 构造器中

**记录日期**: 2026-05-21

## 天赋面板数据不刷新

**现象**: 使用下界之星增加星光层数后，天赋面板显示的数值不变。

**原因**: `PlayerTalentUI.getPlayerTalents()` 使用缓存，仅根据"解锁数量"判断缓存是否有效。星光层数变化不会触发缓存失效。

**修复**: 移除天赋列表缓存，每帧重建。面板仅在背包打开时渲染，性能影响可忽略。

**记录日期**: 2026-05-21

## 退出重进天赋丢失

**现象**: 解锁天赋后退出游戏重进，天赋面板显示"没有已解锁的天赋"。

**原因**: `UnlockManager` 使用静态 `HashMap<UUID, Set<ResourceLocation>>`，数据存在内存中，未持久化到磁盘。

**修复**: 创建 `UnlockSavedData` (extends `SavedData`)，通过 `DimensionDataStorage` 保存到世界存档。在 `LevelEvent.Load` 时加载、`LevelEvent.Save` 时写入。`UnlockManager.unlock()` 自动标记脏数据。

**记录日期**: 2026-05-21

## 客户端看不到玩家数据变更

**现象**: 服务端调用 `PlayerDataAPI.set()` 后，客户端通过 `get()` 读取仍是旧值。

**原因**: `AttachmentType` 的数据只保存在服务端玩家对象上，不同步到客户端玩家。

**修复**: 创建 `SyncPlayerDataPayload` 网络包。`PlayerDataAPI.set()` 通过回调自动发送 S2C 包，客户端收到后更新本地玩家的 Attachment。

**记录日期**: 2026-05-21

## 窗口内容溢出

**现象**: 天赋面板缩小后，详情行文字超出窗口内容区。

**原因**: 预裁剪检查只在整条天赋层面做，没有考虑详情行超出边界的情况。

**修复**: 改为先计算整条天赋的完整高度（标准行 + 详情行），如果不能完整显示则跳过该天赋。

**记录日期**: 2026-05-21

## 根目录旧版 mixins.json

**现象**: 项目根目录有一个只包含 3 个 mixin 的旧版 `yizmodqzk.mixins.json`（缺少 `FlightOptimizationMixin` 和 `NoCollisionMixin`）。

**影响**: 如果 IDE 意外将根目录加入资源路径，两个 mixin 不会生效。

**建议**: 删除根目录的旧版文件，只保留 `src/main/resources/` 下的完整版（5 个 mixin）。

## flatDir 仓库无法解析 Maven 结构

**现象**: 下游模组使用 `flatDir` 指向主模组的 `repo/` 目录，但 `./gradlew publish` 生成的是 Maven 目录结构。

**原因**: `flatDir` 只在目录根找 `.jar` 文件，不会遍历 `net/minecraft/client/yiz/` 子目录。

**修复**: 改用 `maven { url = 'file:///path/to/repo' }` 代替 `flatDir`。
