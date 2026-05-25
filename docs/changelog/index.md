# 变更日志

最后更新: 2026-05-26 00:37

来源仓库: `D:/ZM/yizgzq/yiz1.21.1`

---

### 2026-05-26 — `28b11300`

feat: creative tab auto-registry — 4母页系统 + 4接口API

### 2026-05-25 — `e7276a4e`

feat: DaoPalace & RealmProgression API — 道宫建筑系统 + 境界跨度框架

### 2026-05-24 — `41b02dbe`

chore: add build_dead/ to .gitignore; remove build_dead from tracking

### 2026-05-24 — `ff83aa53`

fix: HumanoidArmorLayerStarMixin now catches unregistered PlayerData key instead of crashing

### 2026-05-24 — `932d3953`

fix: add neo_version_range to replaceProperties for template expansion

### 2026-05-24 — `3c8ad7e2`

fix: 8 P1 code quality issues

### 2026-05-24 — `8dec58a5`

fix: P0 bugs across damage/effect/mixin modules

### 2026-05-24 — `80155a29`

relax Neo version range to [21.1,22.0) — accept entire 21.x series

### 2026-05-24 — `95b7d145`

relax Neo version range to [21.1.227,21.2) in mods.toml

### 2026-05-24 — `d1f60ca1`

add cosmic3 and cosmic4 shader pipeline files

### 2026-05-24 — `9ad47680`

normalize line endings

### 2026-05-24 — `0f957f11`

fix: shader rendering + flight API + NeoForge version rollback

### 2026-05-23 — `4539319d`

fix: star armor rendering — split z/non-z pipeline, fix depth write & alpha

### 2026-05-22 — `e2497663`

fix: flight speed 1.2x + instant stop on key release

### 2026-05-22 — `4a9eee03`

feat: cosmic2 shader preset — star flares + HSV nebula

### 2026-05-22 — `c19c3926`

feat: ShaderManager — central shader preset registry with runtime switching

### 2026-05-22 — `ee7ed09c`

fix: shader compilation — GLSL simplification, armor null-guard, uniform naming

### 2026-05-22 — `6d08c6f6`

feat: shader rendering system — star film overlay via core shaders

### 2026-05-22 — `384481b7`

docs: add architecture blueprint ref + current focus area to CLAUDE.md

### 2026-05-22 — `6c5df5e9`

docs: add AI quick entry for YIZwikl docs site

### 2026-05-22 — `750e14b0`

更新 CLAUDE.md：补充注册表 API 文档（10 个 Registry + PlayerDataAPI）

### 2026-05-21 — `04ef23c8`

修复 GeckoLib 冲突 + 天赋面板 UI 联动 + 数据持久化与同步

### 2026-05-19 — `45b69061`

清理旧 GUI 资源 + 移除旧武器/天赋类 + 新增架构审查文档 + 新增 network 网络同步包

### 2026-05-16 — `862a8501`

新增 Unsafe 实例级保护系统 + 整理 CLAUDE.md

### 2026-05-16 — `59095715`

更新 CLAUDE.md：新增攻击目标锁定 + 物品属性系统章节

### 2026-05-16 — `a32235d9`

新增攻击目标锁定 + 物品属性系统 + 简易指令注册 + %伤害增幅/减免 Mixin

### 2026-05-16 — `4d28d1be`

清理残余功能 + 新增物品属性系统 + 简易指令注册 + %伤害增幅/减免 Mixin 集成

### 2026-05-16 — `5fd1e873`

Implement High-Level Smithing GUI with texture block compositing

### 2026-05-16 — `db0f0de9`

Refactor container data persistence into formal namespaced API

### 2026-05-16 — `cf45c3b4`

Restructure GUI system: refactor container classes and UI config

### 2026-05-15 — `f1650673`

Refactor test chest into dynamic container system with texture atlas planning

### 2026-05-14 — `d78738a4`

Add GUI texture block system: interactive test container with slot click fix

### 2026-05-14 — `cc287178`

Add distribution package task and API doc with integration guide

### 2026-05-14 — `bab72e75`

Add special damage API (true/armor-piercing/pierce-invulnerability) and CoreMod heal ban fallback

### 2026-05-14 — `15bb7e80`

Fix heal ban tick enforcement to use itemsById reflection for Titan Float channel coverage

### 2026-05-14 — `988fa052`

Implement ASM-level heal ban and tick enforcement for Titan compatibility

### 2026-05-14 — `36b7ac91`

Add public API: attribute-binding damage system and direct health modification

### 2026-05-14 — `9ddd6e7a`

Add universal health channel scanner and public API

### 2026-05-11 — `70b87719`

Fix ASM Agent loading and implement Reimu attribute-to-health pipeline

### 2026-05-11 — `3ca13fc1`

Implement health modification system with three-layer architecture

### 2026-05-11 — `43b501ec`

Purge test code and debug messages

### 2026-05-11 — `d9574827`

Refactor talent UI panel into resizable, draggable window

### 2026-05-11 — `d39c9724`

Fix AttackContext tag detection and attribute modifier scheduling

### 2026-05-11 — `1623e562`

Fix item perception to check NBT binding, unify UI tooltip styling

### 2026-05-11 — `843a9ae3`

Fix mixin: hurt() callback needs CallbackInfoReturnable<Boolean>

### 2026-05-11 — `aa471eec`

Add test effects and fix library design issues

### 2026-05-11 — `7e6bc21c`

Initial commit: YizMod QZK Library Framework

### 2026-05-11 — `a068f346`

Initial commit
