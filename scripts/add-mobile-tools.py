from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')
marker = 'DUSKREEL-MOBILE-EDITOR-FIX-V7'
if marker in s:
    print('V7 already installed')
    raise SystemExit(0)

css = r'''
<style id="duskreel-mobile-editor-fix-v7">
/* DUSKREEL-MOBILE-EDITOR-FIX-V7 */
@media(max-width:760px){
 html,body,#app{width:100%;height:100dvh!important;min-height:100dvh!important;overflow:hidden!important}
 main{height:calc(100dvh - 50px)!important;min-height:0!important;display:flex!important;flex-direction:column!important;overflow:hidden!important}
 main .rail{display:none!important}
 main .panel,.panel.lightroom-panel{display:block!important;order:4!important;flex:1 1 auto!important;width:100%!important;height:auto!important;min-height:0!important;max-height:none!important;overflow-y:auto!important;overflow-x:hidden!important;padding-bottom:110px!important;-webkit-overflow-scrolling:touch!important}
 .stage,.clean-stage{order:1!important;position:relative!important;width:100%!important;flex:0 0 40dvh!important;height:40dvh!important;min-height:230px!important;max-height:390px!important;padding:6px!important;margin:0!important;background:#080808!important;overflow:hidden!important;display:flex!important;align-items:center!important;justify-content:center!important}
 .before-after{width:100%!important;height:100%!important;display:flex!important;flex-direction:row!important;align-items:stretch!important;justify-content:stretch!important}
 .compare-pane{position:relative!important;flex:1 1 50%!important;width:50%!important;height:100%!important;min-width:0!important;display:flex!important;align-items:center!important;justify-content:center!important;overflow:hidden!important;background:#080808!important}
 .compare-pane+.compare-pane{border-left:2px solid #242428!important}
 .compare-pane canvas,#work,#beforeWork{display:block!important;max-width:96%!important;max-height:37dvh!important;width:auto!important;height:auto!important;object-fit:contain!important}
 .compare-divider{display:block!important;width:2px!important;flex:0 0 2px!important;background:#242428!important}
 .compare-label{position:absolute!important;left:7px!important;top:7px!important;z-index:20!important;padding:4px 7px!important;border-radius:5px!important;background:rgba(0,0,0,.75)!important;color:#fff!important;font-size:10px!important;font-weight:700!important}
 body.dusk-has-photos #stageEmpty,body.dusk-has-photos #dropZone,body.dusk-has-photos .stage-empty,body.dusk-has-photos .mobile-upload-actions{display:none!important}
 .filmstrip{order:2!important;flex:0 0 52px!important;height:52px!important;min-height:52px!important;width:100%!important;overflow-x:auto!important;overflow-y:hidden!important}
 #mobileEditTools{order:3!important;flex:0 0 70px!important;height:70px!important;width:100%!important;display:flex!important;overflow-x:auto!important;overflow-y:hidden!important}
 #duskPixelDock{order:3!important;position:relative!important;width:100%!important;bottom:auto!important;left:auto!important;right:auto!important;z-index:1000!important}
 .mobile-app-nav{display:flex!important;z-index:4000!important}
 .mobile-app-nav button[data-mobile-action="download"]{display:flex!important;visibility:visible!important;opacity:1!important}
 .export-bar{display:flex!important;visibility:visible!important;opacity:1!important}
}
@media(max-width:430px){
 .stage,.clean-stage{flex-basis:38dvh!important;height:38dvh!important;min-height:215px!important;max-height:290px!important}
 .compare-pane canvas,#work,#beforeWork{max-width:94%!important;max-height:35dvh!important}
 #mobileEditTools{flex-basis:68px!important;height:68px!important}
}
</style>
'''

js = r'''
<script id="duskreel-mobile-editor-fix-v7-js">
(function(){
 function loaded(){
   var thumbs=document.querySelectorAll('.filmstrip img,.filmstrip .thumb,#thumbList .thumb');
   for(var i=0;i<thumbs.length;i++) if(thumbs[i].naturalWidth>0 || thumbs[i].querySelector?.('img')) return true;
   return /\b[1-9][0-9]*\s+photos?\s+loaded\b/i.test(document.body.innerText||'');
 }
 function sync(){
   if(innerWidth>760)return;
   /* Remove the earlier fake image overlay. Use Duskreel's real before/after canvases. */
   var fake=document.getElementById('duskBeforeAfter');
   if(fake)fake.remove();
   var oldStyle=document.getElementById('duskreel-mobile-before-after-v5');
   if(oldStyle)oldStyle.remove();
   var yes=loaded();
   document.body.classList.toggle('dusk-has-photos',yes);
   var empty=document.getElementById('stageEmpty')||document.getElementById('dropZone');
   if(empty)empty.style.setProperty('display',yes?'none':'','important');
   var ba=document.getElementById('beforeAfter');
   if(ba && yes)ba.style.setProperty('display','flex','important');
 }
 function init(){
   sync();
   new MutationObserver(sync).observe(document.body,{subtree:true,childList:true,attributes:true,characterData:true,attributeFilter:['style','class','src']});
   setInterval(sync,700);
 }
 if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();
})();
</script>
'''

s = s.replace('</head>', css + '\n</head>', 1)
s = s.replace('</body>', js + '\n</body>', 1)
p.write_text(s, encoding='utf-8')
print('Installed V7 mobile editor fix: real preview, download, and half-screen before/after')
