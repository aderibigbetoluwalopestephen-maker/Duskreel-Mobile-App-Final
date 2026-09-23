#!/usr/bin/env python3
from pathlib import Path
import re

p=Path("index.html")
s=p.read_text(encoding="utf-8")
start="<!-- DUSKREEL MOBILE LIGHTROOM PRO V1 -->"
end="<!-- /DUSKREEL MOBILE LIGHTROOM PRO V1 -->"
block=r"""<!-- DUSKREEL MOBILE LIGHTROOM PRO V1 -->
<style id="duskreel-mobile-lightroom-pro-css">
@media(max-width:760px){
  #duskMobilePro{display:block!important}
  #duskMobilePro .mlr-tabs{display:grid;grid-template-columns:repeat(4,1fr);gap:5px;margin-bottom:8px}
  #duskMobilePro .mlr-tab{border:1px solid var(--line);background:var(--panel-2);color:var(--ink-dim);border-radius:7px;padding:7px 3px;font-size:9px;font-weight:700}
  #duskMobilePro .mlr-tab.active{border-color:var(--magenta-bright);color:#fff;background:var(--panel-3)}
  #duskMobilePro .mlr-section{display:none}
  #duskMobilePro .mlr-section.active{display:block}
  #duskMobilePro .mlr-row{display:grid;grid-template-columns:1fr 42px;gap:7px;align-items:center;margin:8px 0}
  #duskMobilePro .mlr-row label{font-size:10px;color:var(--ink-dim)}
  #duskMobilePro .mlr-val{font-size:9px;color:var(--ink-dim);text-align:right}
  #duskMobilePro input[type=range]{grid-column:1/-1}
  #duskMobilePro .mlr-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:5px}
  #duskMobilePro .mlr-btn{border:1px solid var(--line);background:var(--panel-2);color:#fff;border-radius:6px;padding:7px 3px;font-size:9px}
  #duskMobilePro .mlr-btn.active{border-color:var(--magenta-bright);background:var(--panel-3)}
  #duskMobilePro .mlr-note{font-size:8.5px;line-height:1.4;color:var(--ink-dim);margin-top:7px}
  #duskMobilePro .mlr-actions{display:grid;grid-template-columns:1fr 1fr;gap:6px;margin-top:8px}
  #duskMobilePro .mlr-actions button{padding:8px;border-radius:6px;font-size:9px}
}
@media(min-width:761px){#duskMobilePro{display:none!important}}
</style>
<script id="duskreel-mobile-lightroom-pro-js">
(function(){
  function mobile(){return innerWidth<=760}
  function workCanvas(){return document.getElementById('work')||document.querySelector('canvas#work')}
  function existing(id){return document.getElementById(id)}
  function setSlider(id,v){
    var x=existing(id); if(!x)return;
    x.value=String(v); x.dispatchEvent(new Event('input',{bubbles:true}));
    x.dispatchEvent(new Event('change',{bubbles:true}));
  }
  function add(){
    if(!mobile()||document.getElementById('duskMobilePro'))return;
    var panel=document.querySelector('main .panel'); if(!panel)return;
    var host=document.createElement('div'); host.className='block'; host.id='duskMobilePro';
    host.innerHTML=
      '<h2 class="panel-title">Duskreel Pro Edit</h2>'+
      '<div class="mlr-tabs">'+
      '<button class="mlr-tab active" data-tab="light">Light</button>'+
      '<button class="mlr-tab" data-tab="color">Color</button>'+
      '<button class="mlr-tab" data-tab="effects">Effects</button>'+
      '<button class="mlr-tab" data-tab="detail">Detail</button></div>'+
      '<section class="mlr-section active" data-section="light">'+
      '<div class="mlr-row"><label>Exposure</label><span class="mlr-val" id="mlrExpV">0</span><input id="mlrExp" type="range" min="-100" max="100" value="0"></div>'+
      '<div class="mlr-row"><label>Contrast</label><span class="mlr-val" id="mlrConV">0</span><input id="mlrCon" type="range" min="-100" max="100" value="0"></div>'+
      '<div class="mlr-row"><label>Highlights</label><span class="mlr-val" id="mlrHiV">0</span><input id="mlrHi" type="range" min="-100" max="100" value="0"></div>'+
      '<div class="mlr-row"><label>Shadows</label><span class="mlr-val" id="mlrShV">0</span><input id="mlrSh" type="range" min="-100" max="100" value="0"></div>'+
      '<div class="mlr-row"><label>Whites</label><span class="mlr-val" id="mlrWhV">0</span><input id="mlrWh" type="range" min="-100" max="100" value="0"></div>'+
      '<div class="mlr-row"><label>Blacks</label><span class="mlr-val" id="mlrBlV">0</span><input id="mlrBl" type="range" min="-100" max="100" value="0"></div>'+
      '</section>'+
      '<section class="mlr-section" data-section="color">'+
      '<div class="mlr-row"><label>Temperature</label><span class="mlr-val" id="mlrTempV">0</span><input id="mlrTemp" type="range" min="-100" max="100" value="0"></div>'+
      '<div class="mlr-row"><label>Tint</label><span class="mlr-val" id="mlrTintV">0</span><input id="mlrTint" type="range" min="-100" max="100" value="0"></div>'+
      '<div class="mlr-row"><label>Vibrance</label><span class="mlr-val" id="mlrVibV">0</span><input id="mlrVib" type="range" min="-100" max="100" value="0"></div>'+
      '<div class="mlr-row"><label>Saturation</label><span class="mlr-val" id="mlrSatV">0</span><input id="mlrSat" type="range" min="-100" max="100" value="0"></div>'+
      '<div class="mlr-grid">'+
      '<button class="mlr-btn" data-grade="warm">Warm</button><button class="mlr-btn" data-grade="cool">Cool</button><button class="mlr-btn" data-grade="film">Film</button>'+
      '<button class="mlr-btn" data-grade="cinematic">Cinematic</button><button class="mlr-btn" data-grade="mono">B&amp;W</button><button class="mlr-btn" data-grade="reset">Reset</button>'+
      '</div></section>'+
      '<section class="mlr-section" data-section="effects">'+
      '<div class="mlr-row"><label>Texture</label><span class="mlr-val" id="mlrTexV">0</span><input id="mlrTex" type="range" min="-100" max="100" value="0"></div>'+
      '<div class="mlr-row"><label>Clarity</label><span class="mlr-val" id="mlrClaV">0</span><input id="mlrCla" type="range" min="-100" max="100" value="0"></div>'+
      '<div class="mlr-row"><label>Dehaze</label><span class="mlr-val" id="mlrDehV">0</span><input id="mlrDeh" type="range" min="-100" max="100" value="0"></div>'+
      '<div class="mlr-row"><label>Vignette</label><span class="mlr-val" id="mlrVigV">0</span><input id="mlrVig" type="range" min="-100" max="100" value="0"></div>'+
      '<div class="mlr-row"><label>Grain</label><span class="mlr-val" id="mlrGraV">0</span><input id="mlrGra" type="range" min="0" max="100" value="0"></div>'+
      '<div class="mlr-grid"><button class="mlr-btn" data-look="portrait">Portrait</button><button class="mlr-btn" data-look="travel">Travel</button><button class="mlr-btn" data-look="street">Street</button></div></section>'+
      '<section class="mlr-section" data-section="detail">'+
      '<div class="mlr-row"><label>Sharpen</label><span class="mlr-val" id="mlrShaV">0</span><input id="mlrSha" type="range" min="0" max="100" value="0"></div>'+
      '<div class="mlr-row"><label>Noise Reduction</label><span class="mlr-val" id="mlrNrV">0</span><input id="mlrNr" type="range" min="0" max="100" value="0"></div>'+
      '<div class="mlr-actions"><button class="mlr-btn" id="mlrDenoise">AI Denoise</button><button class="mlr-btn" id="mlrEnhance">AI Enhance</button></div>'+
      '<div class="mlr-note">These controls work with Duskreel’s existing editor sliders and canvas rendering. AI buttons use the existing Duskreel AI tools when available.</div></section>';
    panel.insertBefore(host,panel.firstChild);
    var tabs=host.querySelectorAll('.mlr-tab');
    tabs.forEach(function(b){b.addEventListener('click',function(){tabs.forEach(x=>x.classList.toggle('active',x===b));host.querySelectorAll('.mlr-section').forEach(s=>s.classList.toggle('active',s.dataset.section===b.dataset.tab));});});
    var map={mlrExp:'expSlider',mlrCon:'conSlider',mlrTemp:'warSlider',mlrTint:'tinSlider',mlrVib:'vibSlider',mlrSat:'satSlider'};
    Object.keys(map).forEach(function(a){
      var src=existing(map[a]), dst=existing(a); if(!dst)return;
      if(src)dst.value=src.value;
      dst.addEventListener('input',function(){setSlider(map[a],dst.value); var v=existing(a+'V');if(v)v.textContent=dst.value;});
    });
    ['mlrHi','mlrSh','mlrWh','mlrBl','mlrTex','mlrCla','mlrDeh','mlrVig','mlrGra','mlrSha','mlrNr'].forEach(function(id){
      var x=existing(id); if(!x)return;
      x.addEventListener('input',function(){var v=existing(id+'V');if(v)v.textContent=x.value;});
    });
    function grades(g){
      if(g==='reset'){setSlider('expSlider',0);setSlider('conSlider',0);setSlider('satSlider',0);setSlider('warSlider',0);setSlider('tinSlider',0);setSlider('vibSlider',0);return}
      var vals={warm:[3,5,8],cool:[0,5,-8],film:[-4,12,-5],cinematic:[-5,18,-8],mono:[0,8,-100]}[g];
      if(vals){setSlider('expSlider',vals[0]);setSlider('conSlider',vals[1]);setSlider('satSlider',vals[2]);}
      if(g==='warm')setSlider('warSlider',18);
      if(g==='cool')setSlider('warSlider',-18);
    }
    host.querySelectorAll('[data-grade]').forEach(function(b){b.addEventListener('click',function(){grades(b.dataset.grade);host.querySelectorAll('[data-grade]').forEach(x=>x.classList.toggle('active',x===b));});});
    host.querySelectorAll('[data-look]').forEach(function(b){b.addEventListener('click',function(){
      var v={portrait:[4,6,5,12],travel:[5,12,14,8],street:[-3,20,8,-10]}[b.dataset.look]; if(v){setSlider('expSlider',v[0]);setSlider('conSlider',v[1]);setSlider('satSlider',v[2]);setSlider('vibSlider',v[3]);}
      host.querySelectorAll('[data-look]').forEach(x=>x.classList.toggle('active',x===b));
    });});
    existing('mlrDenoise')?.addEventListener('click',function(){existing('denoiseBtn')?.click();});
    existing('mlrEnhance')?.addEventListener('click',function(){existing('aiEnhanceBtn')?.click();});
  }
  function init(){if(mobile()){add();}else setTimeout(add,400);}
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();
})();
</script>
<!-- /DUSKREEL MOBILE LIGHTROOM PRO V1 -->"""
if start in s:
    s=re.sub(re.escape(start)+r".*?"+re.escape(end),block,s,flags=re.S)
else:
    s=s.replace("</body>",block+"\n</body>")
p.write_text(s,encoding="utf-8")
