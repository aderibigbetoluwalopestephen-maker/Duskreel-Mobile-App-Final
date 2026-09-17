from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')
marker = 'DUSKREEL-MOBILE-BEFORE-AFTER-FIX-V5'
if marker in s:
    print('V5 mobile canvas fix already installed')
    raise SystemExit(0)

css = r'''
<style id="duskreel-mobile-before-after-v5">
/* DUSKREEL-MOBILE-BEFORE-AFTER-FIX-V5 */
@media (max-width:760px){
  html,body,#app{width:100%;height:100dvh!important;min-height:100dvh!important;overflow:hidden!important;}
  main{height:calc(100dvh - 50px)!important;min-height:0!important;display:flex!important;flex-direction:column!important;overflow:hidden!important;}
  .rail,.panel,.lightroom-panel,.right-panel,.adjustments-panel,.sidebar-right{display:none!important;}
  .stage,.clean-stage{order:1!important;position:relative!important;top:auto!important;left:auto!important;right:auto!important;bottom:auto!important;width:100%!important;flex:1 1 auto!important;height:auto!important;min-height:0!important;max-height:none!important;padding:6px!important;margin:0!important;background:#080808!important;overflow:hidden!important;}
  /* The original upload card is only for an empty editor. */
  body.dusk-has-photos #stageEmpty,body.dusk-has-photos #dropZone,body.dusk-has-photos .stage-empty,body.dusk-has-photos .drop,body.dusk-has-photos .mobile-upload-actions{display:none!important;}
  #duskBeforeAfter{position:absolute!important;inset:6px!important;z-index:20!important;display:none!important;width:auto!important;height:auto!important;background:#050505!important;overflow:hidden!important;}
  body.dusk-has-photos #duskBeforeAfter{display:flex!important;flex-direction:row!important;}
  #duskBeforeAfter .dba-pane{position:relative!important;flex:1 1 50%!important;width:50%!important;height:100%!important;min-width:0!important;min-height:0!important;display:flex!important;align-items:center!important;justify-content:center!important;overflow:hidden!important;background:#080808!important;}
  #duskBeforeAfter .dba-pane+.dba-pane{border-left:2px solid #080808!important;}
  #duskBeforeAfter img{display:block!important;width:100%!important;height:100%!important;max-width:100%!important;max-height:100%!important;object-fit:contain!important;}
  #duskBeforeAfter .dba-label{position:absolute!important;left:7px!important;top:7px!important;padding:4px 7px!important;border-radius:5px!important;background:rgba(0,0,0,.72)!important;color:#fff!important;font-size:10px!important;font-weight:700!important;z-index:30!important;}
  #work,#beforeWork,.compare-pane canvas{max-width:100%!important;max-height:100%!important;object-fit:contain!important;}
  .filmstrip{order:2!important;flex:0 0 48px!important;height:48px!important;min-height:48px!important;width:100%!important;overflow-x:auto!important;overflow-y:hidden!important;}
  #duskPixelDock{order:3!important;position:relative!important;left:auto!important;right:auto!important;bottom:auto!important;width:100%!important;height:126px!important;flex:0 0 126px!important;z-index:100!important;}
  #duskPixelTools{height:72px!important;flex:0 0 72px!important;overflow-x:auto!important;}
  .dpt-categories{height:54px!important;flex:0 0 54px!important;overflow-x:auto!important;}
  .export-bar{display:none!important;}
}
@media (min-width:761px){#duskBeforeAfter{display:none!important;}}
</style>
'''

html = r'''
<!-- DUSKREEL-MOBILE-BEFORE-AFTER-FIX-V5 -->
<div id="duskBeforeAfter" aria-label="Before and after preview">
  <div class="dba-pane"><span class="dba-label">Before</span><img id="duskBeforeImg" alt="Before preview"></div>
  <div class="dba-pane"><span class="dba-label">After</span><img id="duskAfterImg" alt="After preview"></div>
</div>
<script id="duskreel-mobile-before-after-script-v5">
(function(){
  function findLoadedPhoto(){
    var n=document.getElementById('exportCount');
    if(n && /[1-9][0-9]*\s+photo(?:s)?\s+loaded/i.test(n.textContent||'')) return true;
    var thumbs=document.querySelectorAll('.filmstrip img, .thumb img, .thumbnail img');
    for(var i=0;i<thumbs.length;i++) if(thumbs[i].naturalWidth>0) return true;
    return false;
  }
  function sync(){
    if(innerWidth>760)return;
    var loaded=findLoadedPhoto();
    document.body.classList.toggle('dusk-has-photos',loaded);
    var wrap=document.getElementById('duskBeforeAfter');
    if(!wrap)return;
    if(loaded){
      wrap.style.setProperty('display','flex','important');
      var src='';
      var original=document.querySelector('main img:not(#duskBeforeImg):not(#duskAfterImg)');
      if(original && original.naturalWidth>0) src=original.currentSrc||original.src;
      if(src){document.getElementById('duskBeforeImg').src=src;document.getElementById('duskAfterImg').src=src;}
    }else{
      wrap.style.setProperty('display','none','important');
    }
  }
  function init(){
    var stage=document.querySelector('main .stage, main .clean-stage');
    var wrap=document.getElementById('duskBeforeAfter');
    if(stage && wrap && wrap.parentElement!==stage) stage.appendChild(wrap);
    sync();
    if(!window.__duskMobileV5){
      window.__duskMobileV5=true;
      var mo=new MutationObserver(sync);
      mo.observe(document.body,{subtree:true,childList:true,attributes:true,characterData:true,attributeFilter:['style','class','src']});
      setInterval(sync,500);
    }
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();
})();
</script>
'''

s = s.replace('</head>', css + '\n</head>', 1)
s = s.replace('</body>', html + '\n</body>', 1)
p.write_text(s, encoding='utf-8')
print('Installed V5 mobile before/after canvas fix')
