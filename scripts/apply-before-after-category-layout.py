from pathlib import Path
import re

path = Path('index.html')
text = path.read_text(encoding='utf-8')

# Remove unstable/duplicate mobile patches. Multiple observers were repeatedly
# changing class/style attributes and could freeze Chrome while selecting a photo.
for ident in [
    'duskreel-before-after-category-layout-v1',
    'duskreel-before-after-category-layout-v1-script',
    'duskreel-mobile-before-after-v5',
    'duskreel-mobile-before-after-script-v5',
    'duskreel-mobile-editor-fix-v6',
    'duskreel-mobile-editor-fix-v6-js',
    'duskreel-mobile-editor-fix-v8',
    'duskreel-mobile-editor-fix-v8-js',
    'duskreel-mobile-professional-v2',
    'duskreel-mobile-professional-v2-js',
    'duskreel-mobile-stable-v9',
    'duskreel-mobile-stable-v9-js',
]:
    text = re.sub(r'<(style|script)[^>]*id=["\']' + re.escape(ident) + r'["\'][^>]*>.*?</\1>\s*', '', text, flags=re.S | re.I)

# Remove duplicate helper markup/scripts from the previous before/after patches.
text = re.sub(r'\s*<div[^>]*id=["\']duskBeforeAfter["\'][^>]*>.*?</div>\s*', '\n', text, flags=re.S | re.I)
text = re.sub(r'<script[^>]*>.*?duskBeforeAfter.*?</script>\s*', '', text, flags=re.S | re.I)

# Remove accidental raw CSS text emitted by the old PixelLab patch.
text = re.sub(r'\\n?/\* DUSKREEL-PIXELLAB-STYLE-TOOLS-V3 \*/.*?(?=<nav[^>]*id=["\']duskPixelDock["\'])', '', text, flags=re.S | re.I)
text = re.sub(r'/\* DUSKREEL-PIXELLAB-STYLE-TOOLS-V3 \*/.*?(?=<style[^>]*duskreel-mobile-editor-fix-v6)', '', text, flags=re.S | re.I)

css = r'''
<style id="duskreel-mobile-stable-v9">
/* DUSKREEL MOBILE STABLE V9 */
@media(max-width:760px){
 html,body{width:100%;height:100%;overflow:hidden!important;background:#0b0b0d!important}
 #app{width:100%;height:100dvh!important;min-height:100dvh!important;display:flex!important;flex-direction:column!important;overflow:hidden!important}
 header{height:50px!important;min-height:50px!important;flex:0 0 50px!important;padding:0 12px!important}
 header .user-pill span{display:none!important}
 main{height:calc(100dvh - 50px)!important;min-height:0!important;display:flex!important;flex-direction:column!important;overflow:hidden!important;position:relative!important}
 main .stage,main .clean-stage{order:1!important;flex:0 0 34dvh!important;height:34dvh!important;min-height:190px!important;max-height:300px!important;width:100%!important;margin:0!important;padding:5px!important;background:#080809!important;overflow:hidden!important}
 .stage-empty{width:100%!important;height:100%!important;display:flex!important;align-items:center!important;justify-content:center!important}
 .stage-empty .drop{width:min(88vw,330px)!important;min-height:132px!important;padding:14px!important;border:1px dashed #a92a86!important;border-radius:14px!important;background:#17171a!important;display:flex!important;flex-direction:column!important;align-items:center!important;justify-content:center!important;gap:5px!important}
 .mobile-upload-actions{display:flex!important;width:100%!important;gap:8px!important;margin-top:5px!important}
 .mobile-upload-actions button{flex:1!important;min-height:40px!important;border-radius:9px!important;border:1px solid #45454c!important;background:#29292d!important;color:#f5f5f6!important;font-weight:700!important;cursor:pointer!important;touch-action:manipulation!important}
 .mobile-upload-actions .primary-upload{background:#f2f2f4!important;color:#111!important;border-color:#fff!important}
 .before-after{width:100%!important;height:100%!important;display:flex!important;flex-direction:row!important;align-items:stretch!important;overflow:hidden!important}
 .compare-pane{flex:1 1 50%!important;width:50%!important;min-width:0!important;height:100%!important;display:flex!important;align-items:center!important;justify-content:center!important;position:relative!important;overflow:hidden!important;background:#080809!important}
 .compare-pane+.compare-pane{border-left:1px solid #333!important}
 .compare-pane canvas,#work,#beforeWork{max-width:96%!important;max-height:32dvh!important;width:auto!important;height:auto!important;object-fit:contain!important}
 .compare-label{position:absolute!important;left:7px!important;top:7px!important;z-index:20!important;padding:3px 6px!important;border-radius:5px!important;background:rgba(0,0,0,.72)!important;color:#fff!important;font-size:9px!important;font-weight:700!important}
 body.dusk-has-photos .stage-empty,body.dusk-has-photos #stageEmpty,body.dusk-has-photos #dropZone,body.dusk-has-photos .mobile-upload-actions{display:none!important}
 main .rail{display:none!important}
 #mobileEditTools{display:none!important}
 .filmstrip{order:2!important;flex:0 0 44px!important;height:44px!important;min-height:44px!important;width:100%!important;padding:3px 7px!important;background:#0e0e10!important;overflow-x:auto!important;overflow-y:hidden!important}
 .filmstrip-meta{height:12px!important;margin-bottom:1px!important;font-size:8px!important}.filmstrip #thumbList{height:27px!important}.filmstrip .thumb{flex:0 0 38px!important;width:38px!important;height:27px!important}
 #duskMobileActions{order:3!important;flex:0 0 48px!important;height:48px!important;width:100%!important;display:flex!important;align-items:center!important;gap:7px!important;padding:5px 8px!important;background:#101014!important;border-top:1px solid #2a2a30!important;border-bottom:1px solid #2a2a30!important;z-index:50!important}
 #duskMobileActions button{flex:1!important;height:36px!important;border-radius:8px!important;border:1px solid #3b3b42!important;font-size:12px!important;font-weight:800!important}.dusk-preview-btn{background:#211a24!important;color:#fff!important}.dusk-download-btn{background:linear-gradient(135deg,#ff4fc3,#e619a6)!important;color:#fff!important;border-color:#ff4fc3!important}
 #duskPixelDock{order:4!important;position:relative!important;left:auto!important;right:auto!important;bottom:auto!important;width:100%!important;height:82px!important;min-height:82px!important;flex:0 0 82px!important;z-index:60!important;background:#111114!important;border-top:1px solid #29292e!important}
 #duskPixelTools{display:none!important}
 .dpt-categories{height:82px!important;min-height:82px!important;width:100%!important;display:flex!important;align-items:flex-start!important;gap:2px!important;padding:7px 5px 5px!important;overflow-x:auto!important;overflow-y:hidden!important;scrollbar-width:none!important;-webkit-overflow-scrolling:touch!important}.dpt-categories::-webkit-scrollbar{display:none!important}
 .dpt-cat{flex:0 0 60px!important;width:60px!important;height:66px!important;padding:5px 2px!important;border:0!important;border-radius:9px!important;background:transparent!important;color:#9999a2!important;display:flex!important;flex-direction:column!important;align-items:center!important;justify-content:center!important;gap:4px!important;font-size:8px!important;font-weight:800!important;white-space:nowrap!important;touch-action:manipulation!important}
 .dpt-cat-icon{width:29px!important;height:29px!important;border-radius:8px!important;background:#232328!important;color:#fff!important;display:flex!important;align-items:center!important;justify-content:center!important;font-size:15px!important;font-weight:800!important}.dpt-cat.active{background:#2b1b2d!important;color:#fff!important}.dpt-cat.active .dpt-cat-icon{background:#ff35b8!important;color:#fff!important}
 main .panel{order:5!important;flex:1 1 auto!important;width:100%!important;min-height:0!important;max-height:none!important;overflow-y:auto!important;overflow-x:hidden!important;background:#0b0b0d!important;padding:8px 9px 12px!important;-webkit-overflow-scrolling:touch!important}.panel.lightroom-panel>.block.mobile-tool-hidden{display:none!important}.panel.lightroom-panel>.block{margin:0 0 7px!important;border:1px solid #28282e!important;border-radius:10px!important;background:#111114!important}
}
@media(max-width:430px){main .stage,main .clean-stage{flex-basis:32dvh!important;height:32dvh!important;min-height:180px!important;max-height:240px!important}.compare-pane canvas,#work,#beforeWork{max-height:29dvh!important}#duskPixelDock{height:76px!important;min-height:76px!important;flex-basis:76px!important}.dpt-categories{height:76px!important;min-height:76px!important;padding-top:5px!important}.dpt-cat{height:64px!important;flex-basis:58px!important;width:58px!important}}
</style>
'''

js = r'''
<script id="duskreel-mobile-stable-v9-js">
(function(){
 function mobile(){return innerWidth<=760;}
 function hasPhoto(){
  var a=document.querySelectorAll('#thumbList img,.filmstrip img');
  for(var i=0;i<a.length;i++)if(a[i].naturalWidth>0||a[i].src)return true;
  var ba=document.getElementById('beforeAfter');
  return !!(ba&&getComputedStyle(ba).display!=='none');
 }
 function sync(){if(!mobile())return;var loaded=hasPhoto();document.body.classList.toggle('dusk-has-photos',loaded);var e=document.getElementById('stageEmpty'),ba=document.getElementById('beforeAfter');if(e)e.style.setProperty('display',loaded?'none':'','important');if(ba&&loaded)ba.style.setProperty('display','flex','important');}
 function uploads(){var d=document.getElementById('dropZone');if(!d||d.querySelector('.mobile-upload-actions'))return;var w=document.createElement('div');w.className='mobile-upload-actions';w.innerHTML='<button type="button" class="primary-upload" data-upload="photos">Add Photos</button><button type="button" data-upload="camera">Camera</button>';d.appendChild(w);w.addEventListener('click',function(e){var b=e.target.closest('button');if(!b)return;e.preventDefault();e.stopPropagation();var x=document.getElementById(b.dataset.upload==='camera'?'cameraInput':'photoInput');if(x)x.click();});}
 function bind(){uploads();var p=document.getElementById('photoInput'),c=document.getElementById('cameraInput');if(p&&!p.dataset.v9){p.dataset.v9='1';p.addEventListener('change',function(){setTimeout(sync,250);});}if(c&&!c.dataset.v9){c.dataset.v9='1';c.addEventListener('change',function(){setTimeout(sync,250);});}sync();setTimeout(sync,900);setTimeout(sync,1800);}
 function dock(){var d=document.getElementById('duskPixelDock');if(!d||d.dataset.v9)return;d.dataset.v9='1';d.querySelectorAll('.dpt-cat').forEach(function(cat){cat.addEventListener('click',function(){d.querySelectorAll('.dpt-cat').forEach(function(x){x.classList.toggle('active',x===cat);});var map={adjust:'#expSlider',effects:'#fxGrid',crop:'#cropTools',ai:'#autoEditBtn',media:'#photoInput',export:'#exportAll',text:'#watermarkBtn',canvas:'#watermarkBtn'},t=document.querySelector(map[cat.dataset.cat]),panel=document.querySelector('main .panel');if(t&&panel)panel.scrollTo({top:Math.max(0,t.closest('.block')?.offsetTop||0),behavior:'smooth'});});});}
 function init(){bind();dock();}
 if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();
})();
</script>
'''

text = text.replace('</head>', css + '\n</head>', 1)
text = text.replace('</body>', js + '\n</body>', 1)
path.write_text(text, encoding='utf-8')
print('Stable V9 mobile cleanup/layout installed.')