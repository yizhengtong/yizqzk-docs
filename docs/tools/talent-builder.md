# 天赋快速构造器

<style>
:root {
  --bg: #f5f5f5;
  --card: #ffffff;
  --border: #e0e0e0;
  --text: #333;
  --muted: #888;
  --accent: #3f51b5;
  --accent-hover: #303f9f;
  --code-bg: #1e1e2e;
  --code-text: #cdd6f4;
  --tag-bg: #e8eaf6;
  --tag-text: #3f51b5;
  --danger: #e53935;
  --success: #43a047;
}
[data-md-color-scheme="slate"] {
  --bg: #1a1a2e;
  --card: #22223a;
  --border: #333;
  --text: #cdd6f4;
  --muted: #888;
  --accent: #7986cb;
  --accent-hover: #9fa8da;
  --code-bg: #11111b;
  --tag-bg: #2a2a4a;
  --tag-text: #7986cb;
}
</style>

<div id="talent-app" style="font-family:var(--md-text-font);color:var(--text);">
<noscript><p style="color:var(--danger)">此工具需要 JavaScript。</p></noscript>

## 基础信息

<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:12px;">
<div>
<label>Mod ID <span style="color:var(--muted);font-size:12px">包路径 + 注册命名空间</span></label>
<input id="modid" type="text" value="yizxianmod" style="width:100%;padding:8px 12px;border:1px solid var(--border);border-radius:6px;background:var(--card);color:var(--text);font-size:14px;">
</div>
<div>
<label>包名 <span style="color:var(--muted);font-size:12px">Java 类所在包</span></label>
<input id="pkg" type="text" value="net.minecraft.client.yiz.xian.effect" style="width:100%;padding:8px 12px;border:1px solid var(--border);border-radius:6px;background:var(--card);color:var(--text);font-size:14px;">
</div>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:12px;margin-bottom:16px;">
<div>
<label>类名</label>
<input id="cls" type="text" value="FlameTouchEffect" style="width:100%;padding:8px 12px;border:1px solid var(--border);border-radius:6px;background:var(--card);color:var(--text);font-size:14px;">
</div>
<div>
<label>效果 ID <span style="color:var(--muted);font-size:12px">ResourceLocation</span></label>
<input id="effid" type="text" value="flame_touch" style="width:100%;padding:8px 12px;border:1px solid var(--border);border-radius:6px;background:var(--card);color:var(--text);font-size:14px;">
</div>
<div>
<label>显示名称</label>
<input id="dispname" type="text" value="烈焰之触" style="width:100%;padding:8px 12px;border:1px solid var(--border);border-radius:6px;background:var(--card);color:var(--text);font-size:14px;">
</div>
</div>

## 六维配置

<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:16px;">

<div>
<label>1. 父类别 ParentType</label>
<select id="parent" style="width:100%;padding:8px 12px;border:1px solid var(--border);border-radius:6px;background:var(--card);color:var(--text);font-size:14px;">
<option value="ECHO">ECHO 残响 — 攻击类效果</option>
<option value="INSCRIPTION">INSCRIPTION 铭刻 — 回复类效果</option>
<option value="MANIFESTATION">MANIFESTATION 显化 — 机制类效果</option>
<option value="ORIGIN">ORIGIN 本形 — 防御类效果</option>
<option value="ASCENSION">ASCENSION 升灵 — 被动类效果</option>
</select>
</div>

<div>
<label>2. 等级 Level</label>
<input id="level" type="number" value="1" min="1" max="100" style="width:100%;padding:8px 12px;border:1px solid var(--border);border-radius:6px;background:var(--card);color:var(--text);font-size:14px;">
</div>

<div>
<label>3. 感知方式 PerceptionMode <span style="color:var(--muted);font-size:12px">OR 逻辑，可多选</span></label>
<div style="display:flex;flex-direction:column;gap:6px;margin-top:4px;">
<label style="display:flex;align-items:center;gap:8px;cursor:pointer;">
  <input type="checkbox" id="perc-entity" checked onchange="toggleEntityOpts()"> EntityPerception — 天赋（需解锁）
</label>
<label style="display:flex;align-items:center;gap:8px;cursor:pointer;">
  <input type="checkbox" id="perc-item" onchange="toggleEntityOpts()"> ItemPerception — 词缀（绑定装备）
</label>
<div id="item-slot-opts" style="display:none;margin-left:24px;">
  <label style="color:var(--muted);font-size:12px;">装备槽位：</label>
  <div style="display:flex;flex-wrap:wrap;gap:6px;">
    <label style="display:flex;align-items:center;gap:4px;font-size:13px;"><input type="checkbox" id="slot-mainhand" checked> MAIN_HAND</label>
    <label style="display:flex;align-items:center;gap:4px;font-size:13px;"><input type="checkbox" id="slot-offhand"> OFF_HAND</label>
    <label style="display:flex;align-items:center;gap:4px;font-size:13px;"><input type="checkbox" id="slot-head"> HEAD</label>
    <label style="display:flex;align-items:center;gap:4px;font-size:13px;"><input type="checkbox" id="slot-chest"> CHEST</label>
    <label style="display:flex;align-items:center;gap:4px;font-size:13px;"><input type="checkbox" id="slot-legs"> LEGS</label>
    <label style="display:flex;align-items:center;gap:4px;font-size:13px;"><input type="checkbox" id="slot-feet"> FEET</label>
    <label style="display:flex;align-items:center;gap:4px;font-size:13px;"><input type="checkbox" id="slot-inventory"> INVENTORY</label>
  </div>
</div>
<label style="display:flex;align-items:center;gap:8px;cursor:pointer;">
  <input type="checkbox" id="perc-container" onchange="toggleEntityOpts()"> ContainerPerception — 随影（绑定容器）
</label>
<div id="container-opts" style="display:none;margin-left:24px;">
  <select id="container-type" style="padding:6px;border:1px solid var(--border);border-radius:4px;background:var(--card);color:var(--text);font-size:13px;">
    <option value="PERSONAL_CONTAINER">PERSONAL_CONTAINER — 任何容器</option>
    <option value="SPECIFIC_CONTAINER">SPECIFIC_CONTAINER — 指定容器类</option>
  </select>
  <input id="container-class" type="text" placeholder="目标容器类全限定名" style="display:none;width:100%;margin-top:4px;padding:6px;border:1px solid var(--border);border-radius:4px;background:var(--card);color:var(--text);font-size:13px;">
</div>
<label style="display:flex;align-items:center;gap:8px;cursor:pointer;">
  <input type="checkbox" id="perc-custom" onchange="toggleEntityOpts()"> CustomPerception — 自定义
</label>
<div id="custom-perc-opts" style="display:none;margin-left:24px;">
  <input id="custom-perc-name" type="text" placeholder="自定义感知类型名" style="width:100%;padding:6px;border:1px solid var(--border);border-radius:4px;background:var(--card);color:var(--text);font-size:13px;">
  <input id="custom-perc-pred" type="text" placeholder="BiPredicate<LivingEntity, EffectContext> 谓词表达式" style="width:100%;margin-top:4px;padding:6px;border:1px solid var(--border);border-radius:4px;background:var(--card);color:var(--text);font-size:13px;">
</div>
</div>
</div>

<div>
<label>4. 触发条件 ActivationCondition</label>
<select id="activation" onchange="toggleCustomActivation()" style="width:100%;padding:8px 12px;border:1px solid var(--border);border-radius:6px;background:var(--card);color:var(--text);font-size:14px;margin-bottom:6px;">
<option value="attack">攻击时 — ctx.target() != null</option>
<option value="hurt">受伤时 — ctx.target() == null</option>
<option value="always">始终 — () -> true</option>
<option value="lowhp">低血量 — entity.getHealth() < entity.getMaxHealth() * 0.3</option>
<option value="kill">击杀时 — 自定义</option>
<option value="custom">自定义条件...</option>
</select>
<textarea id="activation-custom" placeholder="输入自定义条件表达式（lambda 体）" style="display:none;width:100%;padding:8px;border:1px solid var(--border);border-radius:6px;background:var(--card);color:var(--text);font-size:13px;height:60px;resize:vertical;"></textarea>
</div>

<div>
<label>5. 稀有度 Rarity</label>
<select id="rarity" style="width:100%;padding:8px 12px;border:1px solid var(--border);border-radius:6px;background:var(--card);color:var(--text);font-size:14px;">
<option value="MYTHIC">MYTHIC 神话 🔴</option>
<option value="LEGENDARY">LEGENDARY 传说 🟠</option>
<option value="EPIC" selected>EPIC 史诗 🟣</option>
<option value="RARE">RARE 精良 🔵</option>
<option value="COMMON">COMMON 平凡 ⚪</option>
</select>
</div>

</div>

## 执行逻辑

<div style="margin-bottom:12px;">
<label>6. execute() 方法体 <span style="color:var(--muted);font-size:12px">EffectContext context 可用</span></label>
<div style="display:flex;gap:6px;margin-bottom:6px;flex-wrap:wrap;">
<button type="button" onclick="insertSnippet('burn')" style="padding:4px 10px;font-size:12px;border:1px solid var(--border);border-radius:4px;background:var(--card);color:var(--text);cursor:pointer;">+点燃</button>
<button type="button" onclick="insertSnippet('damage')" style="padding:4px 10px;font-size:12px;border:1px solid var(--border);border-radius:4px;background:var(--card);color:var(--text);cursor:pointer;">+伤害</button>
<button type="button" onclick="insertSnippet('heal')" style="padding:4px 10px;font-size:12px;border:1px solid var(--border);border-radius:4px;background:var(--card);color:var(--text);cursor:pointer;">+治疗</button>
<button type="button" onclick="insertSnippet('potion')" style="padding:4px 10px;font-size:12px;border:1px solid var(--border);border-radius:4px;background:var(--card);color:var(--text);cursor:pointer;">+药水效果</button>
<button type="button" onclick="insertSnippet('explosion')" style="padding:4px 10px;font-size:12px;border:1px solid var(--border);border-radius:4px;background:var(--card);color:var(--text);cursor:pointer;">+爆炸</button>
<button type="button" onclick="insertSnippet('lightning')" style="padding:4px 10px;font-size:12px;border:1px solid var(--border);border-radius:4px;background:var(--card);color:var(--text);cursor:pointer;">+雷击</button>
<button type="button" onclick="insertSnippet('velocity')" style="padding:4px 10px;font-size:12px;border:1px solid var(--border);border-radius:4px;background:var(--card);color:var(--text);cursor:pointer;">+击飞</button>
</div>
<textarea id="execbody" style="width:100%;padding:10px;border:1px solid var(--border);border-radius:6px;background:var(--card);color:var(--text);font-family:monospace;font-size:13px;height:120px;resize:vertical;">if (context.target() instanceof LivingEntity target) {
    target.setSecondsOnFire(5);
}</textarea>
</div>

<label>天赋面板详情行（可选，支持 § 颜色代码）</label>
<textarea id="detaillines" placeholder='每行一个详情条目，如：§c使目标燃烧 5 秒' style="width:100%;padding:8px;border:1px solid var(--border);border-radius:6px;background:var(--card);color:var(--text);font-size:13px;height:60px;resize:vertical;">§c使目标燃烧 5 秒</textarea>

<div style="margin-top:16px;display:flex;gap:12px;align-items:center;">
<button onclick="generate()" style="padding:10px 28px;background:var(--accent);color:white;border:none;border-radius:6px;font-size:15px;cursor:pointer;font-weight:600;">生成 Java 代码</button>
<button onclick="copyCode()" id="copy-btn" style="padding:10px 20px;border:1px solid var(--border);border-radius:6px;background:var(--card);color:var(--text);font-size:14px;cursor:pointer;">复制代码</button>
<span id="copy-msg" style="color:var(--success);font-size:13px;display:none;">已复制!</span>
</div>

## 生成的代码

<pre id="output" style="background:var(--code-bg);color:var(--code-text);padding:16px;border-radius:8px;overflow-x:auto;font-size:13px;line-height:1.5;min-height:100px;white-space:pre-wrap;word-break:break-all;">点击上方「生成 Java 代码」按钮查看结果</pre>

</div>

<script>
function toggleEntityOpts() {
  document.getElementById('item-slot-opts').style.display = document.getElementById('perc-item').checked ? 'block' : 'none';
  var cc = document.getElementById('perc-container').checked;
  document.getElementById('container-opts').style.display = cc ? 'block' : 'none';
  if (cc) {
    var ct = document.getElementById('container-type');
    document.getElementById('container-class').style.display = ct.value === 'SPECIFIC_CONTAINER' ? 'block' : 'none';
  }
  document.getElementById('custom-perc-opts').style.display = document.getElementById('perc-custom').checked ? 'block' : 'none';
}

document.getElementById('container-type').onchange = function() {
  document.getElementById('container-class').style.display = this.value === 'SPECIFIC_CONTAINER' ? 'block' : 'none';
};

function toggleCustomActivation() {
  document.getElementById('activation-custom').style.display =
    document.getElementById('activation').value === 'custom' ? 'block' : 'none';
}

function getActivation() {
  var val = document.getElementById('activation').value;
  if (val === 'custom') return document.getElementById('activation-custom').value || 'true /* TODO */';
  switch(val) {
    case 'attack': return 'ctx -> ctx.target() != null';
    case 'hurt': return 'ctx -> ctx.target() == null';
    case 'always': return 'ctx -> true';
    case 'lowhp': return 'ctx -> ctx.entity().getHealth() < ctx.entity().getMaxHealth() * 0.3f';
    case 'kill': return 'ctx -> ctx.target() != null && !ctx.target().isAlive()';
    default: return 'ctx -> true';
  }
}

function getPerceptions() {
  var parts = [];
  if (document.getElementById('perc-entity').checked) parts.push('new EntityPerception()');
  if (document.getElementById('perc-item').checked) {
    var slots = [];
    var slotIds = ['mainhand','offhand','head','chest','legs','feet','inventory'];
    var slotNames = ['MAIN_HAND','OFF_HAND','HEAD','CHEST','LEGS','FEET','INVENTORY'];
    for (var i = 0; i < slotIds.length; i++) {
      if (document.getElementById('slot-' + slotIds[i]).checked) slots.push('ItemPerception.ItemSlot.' + slotNames[i]);
    }
    if (slots.length === 0) slots.push('ItemPerception.ItemSlot.MAIN_HAND');
    parts.push('new ItemPerception(' + slots.join(', ') + ')');
  }
  if (document.getElementById('perc-container').checked) {
    var ct = document.getElementById('container-type').value;
    if (ct === 'SPECIFIC_CONTAINER') {
      parts.push('new ContainerPerception(ContainerPerception.ContainerType.SPECIFIC_CONTAINER, ' + (document.getElementById('container-class').value || 'ChestMenu.class') + ')');
    } else {
      parts.push('new ContainerPerception(ContainerPerception.ContainerType.PERSONAL_CONTAINER)');
    }
  }
  if (document.getElementById('perc-custom').checked) {
    var name = document.getElementById('custom-perc-name').value || 'myCustom';
    var pred = document.getElementById('custom-perc-pred').value || '(entity, ctx) -> true';
    parts.push('CustomPerception.of("' + name + '", ' + pred + ')');
  }
  if (parts.length === 0) parts.push('new EntityPerception()');
  return 'Set.of(' + parts.join(',\n        ') + ')';
}

function generate() {
  var modId = document.getElementById('modid').value.trim() || 'mymod';
  var pkg = document.getElementById('pkg').value.trim() || 'net.minecraft.client.yiz.xian.effect';
  var cls = document.getElementById('cls').value.trim() || 'MyEffect';
  var effId = document.getElementById('effid').value.trim() || 'my_effect';
  var dispName = document.getElementById('dispname').value.trim() || '我的效果';
  var transKey = 'effect.' + modId + '.' + effId;
  var parent = document.getElementById('parent').value;
  var level = document.getElementById('level').value;
  var perceptions = getPerceptions();
  var activation = getActivation();
  var rarity = document.getElementById('rarity').value;
  var execBody = document.getElementById('execbody').value || '// TODO: implement';
  var detailLines = document.getElementById('detaillines').value.trim();

  var needsItemSlot = document.getElementById('perc-item').checked;
  var needsContainer = document.getElementById('perc-container').checked;

  var imports = [
    'import net.minecraft.client.yiz.effect.AbstractEffect;',
    'import net.minecraft.client.yiz.effect.EffectContext;',
    'import net.minecraft.client.yiz.effect.parent.ParentType;',
    'import net.minecraft.client.yiz.effect.rarity.Rarity;',
    'import net.minecraft.resources.ResourceLocation;'
  ];
  if (document.getElementById('perc-entity').checked)
    imports.push('import net.minecraft.client.yiz.effect.perception.EntityPerception;');
  if (needsItemSlot)
    imports.push('import net.minecraft.client.yiz.effect.perception.ItemPerception;');
  if (needsContainer)
    imports.push('import net.minecraft.client.yiz.effect.perception.ContainerPerception;');
  if (document.getElementById('perc-custom').checked)
    imports.push('import net.minecraft.client.yiz.effect.perception.CustomPerception;');

  imports.push('import net.minecraft.world.entity.LivingEntity;');
  imports.push('import java.util.List;');
  imports.push('import java.util.Set;');

  var hasDetail = detailLines.length > 0;
  var detailMethod = '';
  if (hasDetail) {
    var lines = detailLines.split('\n').filter(function(l) { return l.trim(); });
    detailMethod = '\n    @Override\n    public List<String> getTalentDetailLines(LivingEntity entity) {\n        return List.of(\n';
    for (var i = 0; i < lines.length; i++) {
      detailMethod += '            "' + lines[i].trim().replace(/"/g, '\\"') + '"';
      detailMethod += (i < lines.length - 1) ? ',\n' : '\n';
    }
    detailMethod += '        );\n    }\n';
  }

  var code = 'package ' + pkg + ';\n\n'
    + imports.join('\n') + '\n\n'
    + '/**\n'
    + ' * ' + dispName + ' — 自动生成于天赋构造器\n'
    + ' * <p>\n'
    + ' * ' + parent + ' | Lv.' + level + ' | ' + rarity + '\n'
    + ' * </p>\n'
    + ' */\n'
    + 'public class ' + cls + ' extends AbstractEffect {\n\n'
    + '    public ' + cls + '() {\n'
    + '        super(\n'
    + '            ResourceLocation.parse("' + modId + ':' + effId + '"),\n'
    + '            "' + transKey + '",\n'
    + '            "' + dispName + '",\n'
    + '            ParentType.' + parent + ',\n'
    + '            ' + level + ',\n'
    + '            ' + perceptions + ',\n'
    + '            ' + activation + ',\n'
    + '            Rarity.' + rarity + '\n'
    + '        );\n'
    + '    }\n'
    + (hasDetail ? detailMethod : '')
    + '\n    @Override\n'
    + '    public void execute(EffectContext context) {\n'
    + indent(execBody, 8)
    + '\n    }\n'
    + '}\n';

  document.getElementById('output').textContent = code;
}

function indent(text, spaces) {
  var prefix = '';
  for (var i = 0; i < spaces; i++) prefix += ' ';
  return text.split('\n').map(function(l) { return l.trim() ? prefix + l : l; }).join('\n');
}

function insertSnippet(type) {
  var ta = document.getElementById('execbody');
  var snippets = {
    burn: 'if (context.target() instanceof LivingEntity target) {\n    target.setSecondsOnFire(5);\n}',
    damage: 'if (context.target() instanceof LivingEntity target) {\n    target.hurt(target.damageSources().magic(), 10.0f);\n}',
    heal: 'context.entity().heal(5.0f);',
    potion: 'if (context.target() instanceof LivingEntity target) {\n    target.addEffect(new MobEffectInstance(MobEffects.MOVEMENT_SLOWDOWN, 100, 1));\n}',
    explosion: 'if (context.target() != null) {\n    context.level().explode(null, context.target().getX(), context.target().getY(), context.target().getZ(), 2.0f, Level.ExplosionInteraction.NONE);\n}',
    lightning: 'if (context.target() != null) {\n    LightningBolt bolt = new LightningBolt(EntityType.LIGHTNING_BOLT, context.level());\n    bolt.setPos(context.target().position());\n    context.level().addFreshEntity(bolt);\n}',
    velocity: 'if (context.target() instanceof LivingEntity target) {\n    target.knockback(2.0, context.entity().getX() - target.getX(), context.entity().getZ() - target.getZ());\n}'
  };
  ta.value = snippets[type] || ta.value;
  ta.focus();
}

function copyCode() {
  var code = document.getElementById('output').textContent;
  if (!code || code.indexOf('点击上方') >= 0) return;
  navigator.clipboard.writeText(code).then(function() {
    var msg = document.getElementById('copy-msg');
    msg.style.display = 'inline';
    setTimeout(function() { msg.style.display = 'none'; }, 2000);
  });
}

// 初始化
toggleEntityOpts();
toggleCustomActivation();
generate();
</script>
