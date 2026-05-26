# 变更日志

最后更新: 2026-05-26 23:41

来源仓库: `D:/ZM/yizgzq/yiz1.21.1`

---

### 2026-05-26 — `881f9d48`

fix: freeze rotation at current angle when ready (inherit state)

### 2026-05-26 — `73ec6101`

feat: stop rotation when ready; use provider textures

### 2026-05-26 — `0eb1c315`

feat: ConeTargetProvider2 with new corner texture set (lock2_*)

### 2026-05-26 — `c05e7c5a`

chore: remove debug logging from EntityLockAPI, SyncLockPayload, tizMod

### 2026-05-26 — `aa04253d`

fix: remove red tint, always white frame; full opaque at charge=1.0

### 2026-05-26 — `a5044590`

fix: brighter red frame color (0.4 instead of 0.2)

### 2026-05-26 — `d3149ceb`

fix: add client-side debug logging for SyncLockPayload + provider

### 2026-05-26 — `1cc87114`

fix: add missing imports + debug logging for effect pipeline

### 2026-05-26 — `f4598ce0`

fix: re-add dispatchContext call in onPlayerTick

### 2026-05-26 — `d0b741d4`

refactor: TargetFrameProvider + TargetFrameManager architecture

### 2026-05-26 — `548fc63b`

feat: restore 60° cone fallback; API lock overrides with charge/ready

### 2026-05-26 — `e2fc3994`

feat: integrate lock frame with charge/ready state via EntityLockAPI

### 2026-05-26 — `6a5e79df`

fix: un-scale corner tex size; restore frame min scale to 40%

### 2026-05-26 — `ddb69c71`

refactor: extract lock frame parameters as API constants + methods

### 2026-05-26 — `3f724456`

feat: slow rotation of targeting frame (~30°/sec around forward axis)

### 2026-05-26 — `3afa0839`

fix: completely invisible within 3 blocks

### 2026-05-26 — `43340529`

fix: piecewise linear alpha — 0g=0%, 3g=18%, 6g=50%, 9g=80%, 12g=100%

### 2026-05-26 — `68ae329b`

fix: swap top-left/right and bottom-left/right corner textures

### 2026-05-26 — `34412c4c`

fix: stronger fade using quadratic alpha curve (t²)

### 2026-05-26 — `b1311222`

feat: near-range shrink + transparency fade for lock frame

### 2026-05-26 — `13269852`

fix: use event PoseStack directly for texture vertices, no RenderSystem set

### 2026-05-26 — `815b0e0a`

feat: replace red cubes with 4 corner textures on targeting frame

### 2026-05-26 — `6af01405`

fix: frame now uses player-facing local coordinate system

### 2026-05-26 — `361b0f17`

fix: remove Z-direction offset, frame centered at entity body center

### 2026-05-26 — `7dbbfe8c`

fix: body center Y at 70% height instead of 50%

### 2026-05-26 — `788be826`

fix: fixed-scale square frame at body center, not entity AABB matching

### 2026-05-26 — `46431bd3`

fix: add Z-depth half to corner positions — front face of bounding box

### 2026-05-26 — `3e8e8b0e`

fix: use actual bounding-box half-width & half-height for corner positions

### 2026-05-26 — `aac1c15c`

fix: use LevelRenderer.renderLineBox same as F3+B hitbox rendering

### 2026-05-26 — `d3623410`

refactor: screen-space lock frame via ScreenEvent overlay

### 2026-05-26 — `9ecb800e`

fix: square targeting frame centered on entity box center

### 2026-05-26 — `0d5d0fe2`

fix: 60° cone targeting, pick entity closest to screen center

### 2026-05-26 — `ecfb3570`

feat: 4 separate corner textures for lock targeting frame

### 2026-05-26 — `efe1af5a`

refactor: 4-corner targeting frame around entity bounding box

### 2026-05-26 — `9a02586a`

fix: upload poseStack to RenderSystem + fixed screen-size scale

### 2026-05-26 — `30fe9634`

fix: use ProjectileUtil ray trace instead of cone scan for lock icon

### 2026-05-26 — `c4b71115`

fix: EntityLockRenderer shows icon on nearest entity within 60° FOV

### 2026-05-26 — `29c95992`

feat: EntityLockAPI — 实体锁定+网络同步+客户端billboard渲染

### 2026-05-26 — `14c511a8`

fix: ItemInfoUI shows real effect level from NBT instead of template level

### 2026-05-26 — `732eb32b`

fix: remove per-tick effect dispatch — effects recalculated on level change

### 2026-05-26 — `7ade2296`

fix: dispatchContext in player tick + unlock check bypass for ItemPerception

### 2026-05-26 — `d5df6683`

fix: all NBT items go to talent tab with custom name + lore

### 2026-05-26 — `c8f81b61`

feat: CreativeTabAutoRegistry auto-generates NBT items per effect

### 2026-05-26 — `07411330`

feat: EffectNBTHandler — add setEffectLevel/getEffectLevel for item level management

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
