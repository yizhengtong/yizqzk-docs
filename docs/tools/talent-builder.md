# 天赋快速构造器

<style>
:root {
  --c-bg:#fff;--c-card:#f8f9fa;--c-border:#dee2e6;--c-text:#212529;
  --c-muted:#6c757d;--c-accent:#3f51b5;--c-on-accent:#fff;
  --c-danger:#dc3545;--c-success:#198754;--c-tag-bg:#e8eaf6;--c-tag-text:#3f51b5;
}
[data-md-color-scheme="slate"] {
  --c-bg:#1a1a2e;--c-card:#22223a;--c-border:#333;--c-text:#cdd6f4;
  --c-muted:#888;--c-accent:#7986cb;--c-on-accent:#111;
  --c-tag-bg:#2a2a4a;--c-tag-text:#7986cb;
}
.tb-form { max-width:720px; color:var(--c-text); }
.tb-section { background:var(--c-card); border:1px solid var(--c-border); border-radius:8px; padding:16px; margin-bottom:14px; }
.tb-section h3 { margin:0 0 12px; font-size:15px; color:var(--c-accent); }
.tb-row { display:flex; gap:10px; flex-wrap:wrap; }
.tb-field { flex:1; min-width:160px; margin-bottom:10px; }
.tb-field label { display:block; font-size:13px; font-weight:600; margin-bottom:4px; }
.tb-field .hint { font-size:11px; color:var(--c-muted); font-weight:400; }
.tb-field input[type=text],
.tb-field input[type=number],
.tb-field textarea,
.tb-field select { width:100%; padding:7px 10px; border:1px solid var(--c-border); border-radius:5px; background:var(--c-bg); color:var(--c-text); font-size:13px; box-sizing:border-box; }
.tb-field textarea { resize:vertical; min-height:60px; }
.tb-check-group { display:flex; flex-wrap:wrap; gap:6px 14px; }
.tb-check-group label { display:flex; align-items:center; gap:5px; font-size:13px; cursor:pointer; }
.tb-check-group input[type=radio],
.tb-check-group input[type=checkbox] { accent-color:var(--c-accent); }
.tb-sub { margin-left:18px; padding:6px 0 0; border-left:2px solid var(--c-border); padding-left:12px; display:none; }
.tb-sub.show { display:block; }
.tb-sub label { font-size:12px; color:var(--c-muted); }
.tb-btn { padding:10px 32px; border:none; border-radius:6px; font-size:15px; font-weight:600; cursor:pointer; }
.tb-btn.primary { background:var(--c-accent); color:var(--c-on-accent); }
.tb-btn.primary:hover { opacity:.85; }
.tb-btn:disabled { opacity:.5; cursor:not-allowed; }
.tb-msg { font-size:13px; margin-left:10px; }
.tb-msg.ok { color:var(--c-success); }
.tb-msg.err { color:var(--c-danger); }
.tb-cd-row { display:none; margin-top:6px; }
.tb-cd-row.show { display:flex; gap:8px; align-items:center; }
</style>

<div class="tb-form" id="app">
<noscript><p style="color:var(--c-danger)">此工具需要 JavaScript。</p></noscript>

<div class="tb-section">
<h3>基础信息</h3>
<div class="tb-row">
<div class="tb-field" style="min-width:250px;">
<label>天赋名称 <span class="hint">最终类名会加上 Effect 后缀</span></label>
<input type="text" id="name" placeholder="例如：烈焰之触" oninput="livePreview()">
</div>
<div class="tb-field">
<label>Mod ID</label>
<input type="text" id="modid" value="yizxianmod" oninput="livePreview()">
</div>
</div>
<div class="tb-row">
<div class="tb-field">
<label>效果 ID <span class="hint">ResourceLocation 路径部分</span></label>
<input type="text" id="effid" placeholder="flame_touch" oninput="livePreview()">
</div>
<div class="tb-field">
<label>包名</label>
<input type="text" id="pkg" value="net.minecraft.client.yiz.xian.effect" oninput="livePreview()">
</div>
</div>
</div>

<div class="tb-section">
<h3>一、父类别 ParentType <span class="hint">单选</span></h3>
<div class="tb-check-group">
<label><input type="radio" name="parent" value="ECHO" checked onchange="livePreview()"> ECHO 残响 — 攻击类</label>
<label><input type="radio" name="parent" value="INSCRIPTION" onchange="livePreview()"> INSCRIPTION 铭刻 — 回复类</label>
<label><input type="radio" name="parent" value="MANIFESTATION" onchange="livePreview()"> MANIFESTATION 显化 — 机制类</label>
<label><input type="radio" name="parent" value="ORIGIN" onchange="livePreview()"> ORIGIN 本形 — 防御类</label>
<label><input type="radio" name="parent" value="ASCENSION" onchange="livePreview()"> ASCENSION 升灵 — 被动类</label>
</div>
</div>

<div class="tb-section">
<h3>二、最大等级</h3>
<div style="display:flex;align-items:center;gap:10px;">
<label style="display:flex;align-items:center;gap:6px;cursor:pointer;">
<input type="checkbox" id="has-level" onchange="toggleLevel();livePreview();"> 启用等级上限
</label>
<input type="number" id="max-level" value="1" min="1" max="100" style="width:80px;" disabled oninput="livePreview()">
<span class="hint">不勾选则默认等级 = 1</span>
</div>
</div>

<div class="tb-section">
<h3>三、感知方式 PerceptionMode <span class="hint">可多选，OR 逻辑</span></h3>
<div class="tb-check-group" style="margin-bottom:8px;">
<label><input type="checkbox" class="perc-toggle" data-target="perc-entity-sub" checked onchange="toggleSub()"> 天赋 EntityPerception（需解锁）</label>
<label><input type="checkbox" class="perc-toggle" data-target="perc-item-sub" onchange="toggleSub()"> 词缀 ItemPerception（绑定装备）</label>
<label><input type="checkbox" class="perc-toggle" data-target="perc-container-sub" onchange="toggleSub()"> 随影 ContainerPerception（绑定容器）</label>
<label><input type="checkbox" class="perc-toggle" data-target="perc-custom-sub" onchange="toggleSub()"> 自定义 CustomPerception</label>
</div>
<div id="perc-item-sub" class="tb-sub">
  <div class="tb-check-group">
    <label><input type="checkbox" class="item-slot" value="MAIN_HAND" checked> 主手 MAIN_HAND</label>
    <label><input type="checkbox" class="item-slot" value="OFF_HAND"> 副手 OFF_HAND</label>
    <label><input type="checkbox" class="item-slot" value="HEAD"> 头盔 HEAD</label>
    <label><input type="checkbox" class="item-slot" value="CHEST"> 胸甲 CHEST</label>
    <label><input type="checkbox" class="item-slot" value="LEGS"> 护腿 LEGS</label>
    <label><input type="checkbox" class="item-slot" value="FEET"> 靴子 FEET</label>
    <label><input type="checkbox" class="item-slot" value="INVENTORY"> 背包 INVENTORY</label>
  </div>
</div>
<div id="perc-container-sub" class="tb-sub">
  <label style="display:flex;align-items:center;gap:8px;">
    <input type="radio" name="container-type" value="PERSONAL_CONTAINER" checked> 任意容器 PERSONAL_CONTAINER
  </label>
  <label style="display:flex;align-items:center;gap:8px;">
    <input type="radio" name="container-type" value="SPECIFIC_CONTAINER"> 指定容器类
  </label>
  <input type="text" id="container-class" placeholder="全限定类名，如 net.minecraft.world.inventory.ChestMenu" style="display:none;width:100%;margin-top:4px;">
</div>
<div id="perc-custom-sub" class="tb-sub">
  <input type="text" id="custom-perc-name" placeholder="自定义感知类型名称" style="width:100%;margin-bottom:4px;">
  <textarea id="custom-perc-pred" placeholder="谓词表达式 (entity, ctx) -> ..." style="width:100%;height:40px;"></textarea>
</div>
</div>

<div class="tb-section">
<h3>四、稀有度 Rarity <span class="hint">单选</span></h3>
<div class="tb-check-group">
<label><input type="radio" name="rarity" value="MYTHIC" onchange="livePreview()"> MYTHIC 神话</label>
<label><input type="radio" name="rarity" value="LEGENDARY" onchange="livePreview()"> LEGENDARY 传说</label>
<label><input type="radio" name="rarity" value="EPIC" checked onchange="livePreview()"> EPIC 史诗</label>
<label><input type="radio" name="rarity" value="RARE" onchange="livePreview()"> RARE 精良</label>
<label><input type="radio" name="rarity" value="COMMON" onchange="livePreview()"> COMMON 平凡</label>
</div>
</div>

<div class="tb-section">
<h3>五、CD 冷却</h3>
<label style="display:flex;align-items:center;gap:8px;cursor:pointer;">
<input type="checkbox" id="has-cd" onchange="toggleCd();livePreview();"> 启用冷却时间
</label>
<div id="cd-row" class="tb-cd-row">
<input type="number" id="cd-ticks" value="100" min="1" style="width:100px;" disabled oninput="livePreview()">
<span style="font-size:13px;">tick（20 tick = 1 秒）</span>
</div>
</div>

<div class="tb-section">
<h3>六、触发条件 <span class="hint">自定义文本描述</span></h3>
<textarea id="activation" placeholder="例如：当 entity 攻击目标时触发、entity 血量低于30%时触发、每 tick 持续触发..." style="width:100%;height:64px;" oninput="livePreview()"></textarea>
</div>

<div class="tb-section">
<h3>七、总体需求 <span class="hint">自然语言描述天赋效果，交由 AI 实现</span></h3>
<textarea id="requirement" placeholder="例如：攻击时使目标燃烧 5 秒，并造成目标最大生命值 10% 的真实伤害。如果目标已经燃烧，额外附加一次爆炸。" style="width:100%;height:80px;" oninput="livePreview()"></textarea>
</div>

<div class="tb-section">
<h3>八、天赋面板详情行 <span class="hint">创造模式悬停显示的描述，支持 § 颜色代码</span></h3>
<textarea id="detaillines" placeholder="每行一个条目，例如：§c使目标燃烧 5 秒&#10;§6目标已燃烧时追加爆炸&#10;§b伤害类型: 真实伤害" style="width:100%;height:72px;" oninput="livePreview()"></textarea>
</div>

<div style="margin-top:12px;display:flex;align-items:center;gap:12px;">
<button class="tb-btn primary" onclick="doPush()">推送</button>
<span id="msg" class="tb-msg"></span>
</div>

<div style="margin-top:16px;">
<details>
<summary style="cursor:pointer;font-size:13px;color:var(--c-muted);">预览生成的 JSON</summary>
<pre id="preview" style="background:var(--c-card);border:1px solid var(--c-border);padding:12px;border-radius:6px;font-size:12px;max-height:300px;overflow:auto;margin-top:6px;">填写表单后自动显示</pre>
</details>
</div>

</div>

<script>
function $(id) { return document.getElementById(id); }

function val(id) { var e=$(id); return e ? (e.type==='checkbox'||e.type==='radio' ? (e.checked?e.value:null) : e.value) : ''; }

function checkedVal(sel) {
  var el = document.querySelector('input[name="'+sel+'"]:checked');
  return el ? el.value : '';
}

function checkedVals(sel) {
  return Array.from(document.querySelectorAll('.'+sel+':checked')).map(function(cb){return cb.value;});
}

function getPerception() {
  var result = [];
  var toggles = document.querySelectorAll('.perc-toggle');
  for (var i=0;i<toggles.length;i++) {
    var cb = toggles[i];
    if (!cb.checked) continue;
    var sub = $(cb.dataset.target);
    if (sub === $('perc-entity-sub')) result.push('EntityPerception');
    if (sub === $('perc-item-sub')) {
      var slots = checkedVals('item-slot');
      result.push('ItemPerception['+(slots.length ? slots.join(',') : 'MAIN_HAND')+']');
    }
    if (sub === $('perc-container-sub')) {
      var ct = checkedVal('container-type');
      if (ct === 'SPECIFIC_CONTAINER') result.push('ContainerPerception['+ct+':'+val('container-class')+']');
      else result.push('ContainerPerception['+ct+']');
    }
    if (sub === $('perc-custom-sub')) {
      result.push('CustomPerception['+(val('custom-perc-name')||'?')+']');
    }
  }
  return result.length ? result : ['EntityPerception'];
}

function buildData() {
  return {
    name: val('name') || '未命名天赋',
    modid: val('modid') || 'yizxianmod',
    effid: val('effid') || '',
    pkg: val('pkg') || 'net.minecraft.client.yiz.xian.effect',
    parent: checkedVal('parent') || 'ECHO',
    maxLevel: $('has-level').checked ? parseInt(val('max-level'))||1 : 1,
    perception: getPerception(),
    rarity: checkedVal('rarity') || 'EPIC',
    cooldown: $('has-cd').checked ? parseInt(val('cd-ticks'))||0 : 0,
    cooldownEnabled: $('has-cd').checked,
    activation: val('activation'),
    requirement: val('requirement'),
    detailLines: val('detaillines'),
    _timestamp: new Date().toISOString()
  };
}

function livePreview() {
  $('preview').textContent = JSON.stringify(buildData(), null, 2);
}

function toggleLevel() { $('max-level').disabled = !$('has-level').checked; }
function toggleCd() { $('cd-ticks').disabled = !$('has-cd').checked; $('cd-row').classList.toggle('show',$('has-cd').checked); }

function toggleSub() {
  var toggles = document.querySelectorAll('.perc-toggle');
  for (var i=0;i<toggles.length;i++) {
    var sub = $(toggles[i].dataset.target);
    if (sub) sub.classList.toggle('show', toggles[i].checked);
  }
  // also check container radio
  var cc = document.querySelector('.perc-toggle[data-target="perc-container-sub"]');
  if (cc && cc.checked) {
    $('container-class').style.display = checkedVal('container-type')==='SPECIFIC_CONTAINER' ? 'block' : 'none';
  }
}

document.addEventListener('change', function(e) {
  if (e.target.name === 'container-type') {
    $('container-class').style.display = e.target.value === 'SPECIFIC_CONTAINER' ? 'block' : 'none';
    livePreview();
  }
});

function doPush() {
  var data = buildData();
  if (!data.name || data.name === '未命名天赋') { showMsg('请填写天赋名称','err'); return; }
  $('msg').textContent = '推送中...';
  fetch('http://localhost:8765/push', {
    method: 'POST',
    headers: {'Content-Type':'application/json'},
    body: JSON.stringify(data)
  })
  .then(function(r){ return r.json(); })
  .then(function(d){
    if (d.ok) showMsg('已推送: '+d.file, 'ok');
    else showMsg('推送失败: '+(d.error||'未知错误'), 'err');
  })
  .catch(function(){
    showMsg('推送失败: 请先启动 python scripts/talent_server.py','err');
  });
}

function showMsg(text, type) {
  var m = $('msg'); m.textContent = text; m.className = 'tb-msg '+(type||'ok');
  setTimeout(function(){ m.textContent=''; }, 5000);
}

toggleLevel(); toggleCd(); toggleSub(); livePreview();
</script>
