from pathlib import Path
import re

p = Path('index.html')
s = p.read_text(encoding='utf-8')
marker = 'DUSKREEL-MOBILE-EDITOR-FIX-V8'
if marker in s:
    print('V8 already installed')
    raise SystemExit(0)

# Remove the conflicting V5/V7 mobile patches. Keep the original editor markup and behavior.
s = re.sub(r'<style[^>]*id=["\']duskreel-mobile-before-after-v5["\'][^>]*>.*?</style>', '', s, flags=re.S|re.I)
s = re.sub(r'<script[^>]*id=["\']duskreel-mobile-before-after-script-v5["\'][^>]*>.*?</script>', '', s, flags=re.S|re.I)
s = re.sub(r'<style[^>]*id=["\']duskreel-mobile-editor-fix-v7["\'][^>]*>.*?</style>', '', s, flags=re.S|re.I)
s = re.sub(r'<script[^>]*id=["\']duskreel-mobile-editor-fix-v7-js["\'][^>]*>.*?</script>', '', s, flags=re.S|re.I)

css = r'''
<style id="duskreel-mobile-editor-fix-v8">
/* DUSKREEL-MOBILE-EDITOR-FIX-V8 */
@media (max-width:760px){
  html,body,#app{width:100%;height:100dvh!important;min-height:100dvh!important;overflow:hidden!important}
  #app{display:flex!important;flex-direction:column!important}
  header{height:52px!important;min-height:52px!important;flex:0 0 52px!important}
  main{height:calc(100dvh - 52px)!important;min-height:0!important;display:flex!important;flex-direction:column!important;overflow:hidden!important;position:relative!important}

  /* Large editing canvas. */
  main .stage,main .clean-stage{
    order:1!important;position:relative!important;display:flex!important;align-items:center!important;justify-content:center!important;
    width:100%!important;height:44dvh!important;min-height:250px!important;max-height:none!important;flex:0 0 44dvh!important;
    margin:0!important;padding:4px!important;overflow:hidden!important;background:#080808!important
  }
  main .stage .before-after,.before-after{
    display:flex!important;flex-direction:row!important;width:100%!important;height:100%!important;
    align-items:stretch!important;justify-content:stretch!important;overflow:hidden!important
  }
  .before-after .compare-pane,.compare-pane{
    flex:1 1 50%!important;width:50%!important;min-width:0!important;height:100%!important;
    display:flex!important;align-items:center!important;justify-content:center!important;position:relative!important;overflow:hidden!important;background:#080808!important
  }
  .before-after .compare-pane + .compare-pane,.compare-pane + .compare-pane{border-left:2px solid #252525!important}
  .compare-pane canvas,#work,#beforeWork{max-width:100%!important;max-height:100%!important;width:auto!important;height:auto!important;object-fit:contain!important}
  .compare-label{display:block!important;position:absolute!important;left:7px!important;top:7px!important;z-index:20!important;padding:4px 7px!important;border-radius:5px!important;background:rgba(0,0,0,.72)!important;color:#fff!important;font-size:10px!important;font-weight:700!important}

  /* The upload card exists only while the editor is empty. */
  body.dusk-has-photos .stage-empty,
  body.dusk-has-photos .drop-zone,
  body.dusk-has-photos .dropzone,
  body.dusk-has-photos #stageEmpty,
  body.dusk-has-photos #dropZone,
  body.dusk-has-photos .mobile-upload-actions{display:none!important}

  /* Keep the real editor panel available for category tools; don't hide it globally. */
  main .rail{display:none!important}
  main .panel{order:5!important;flex:1 1 auto!important;width:100%!important;min-height:0!important;max-height:none!important;overflow-y:auto!important;overflow-x:hidden!important;-webkit-overflow-scrolling:touch!important;padding-bottom:8px!important}

  /* Thumbnail strip directly below the canvas. */
  .filmstrip{order:2!important;flex:0 0 46px!important;height:46px!important;min-height:46px!important;width:100%!important;overflow-x:auto!important;overflow-y:hidden!important}

  /* Preview / Download are always visible on mobile. */
  #duskMobileActions{order:3!important;flex:0 0 50px!important;height:50px!important;width:100%!important;display:flex!important;align-items:center!important;gap:8px!important;padding:6px 10px!important;background:#100c12!important;border-top:1px solid #35213b!important;border-bottom:1px solid #35213b!important;z-index:2000!important}
  #duskMobileActions button{flex:1 1 50%!important;height:38px!important;border:1px solid #4a2a52!important;border-radius:9px!important;background:#29252b!important;color:#fff!important;font-weight:700!important;font-size:13px!important;cursor:pointer!important}
  #duskMobileActions .dusk-preview-btn{background:#211a24!important}
  #duskMobileActions .dusk-download-btn{background:linear-gradient(135deg,#ff4fc3,#e619a6)!important;border-color:#ff4fc3!important}

  /* Existing PixelLab-style dock remains below the action row. */
  #duskPixelDock{order:4!important;position:relative!important;left:auto!important;right:auto!important;bottom:auto!important;width:100%!important;height:126px!important;min-height:126px!important;flex:0 0 126px!important;z-index:1500!important}
  #duskPixelTools{height:72px!important;min-height:72px!important}
  .dpt-categories{height:54px!important;min-height:54px!important}
  .export-bar{display:none!important}
}
@media (max-width:430px){
  main .stage,main .clean-stage{height:43dvh!important;flex-basis:43dvh!important;min-height:235px!important}
  #duskMobileActions{flex-basis:48px!important;height:48px!important}
  #duskPixelDock{height:122px!important;min-height:122px!important;flex-basis:122px!important}
  #duskPixelTools{height:69px!important;min-height:69px!important}
  .dpt-categories{height:53px!important;min-height:53px!important}
}
</style>
'''

js = r'''
<script id="duskreel-mobile-editor-fix-v8-js">
(function(){
  function hasLoadedPhoto(){
    var thumbs=document.querySelectorAll('.filmstrip img,.thumb img,.thumbnail img,#thumbList img');
    for(var i=0;i<thumbs.length;i++) if(thumbs[i].naturalWidth>0) return true;
    var text=(document.body.innerText||'');
    return /\b[1-9][0-9]*\s+photos?\s+loaded\b/i.test(text);
  }
  function hideUploadCard(){
    if(!hasLoadedPhoto()) return;
    var all=document.querySelectorAll('body *');
    for(var i=0;i<all.length;i++){
      var el=all[i];
      var t=(el.textContent||'').trim();
      if(!/^Drop photos here/i.test(t)) continue;
      var node=el;
      for(var depth=0;depth<6 && node;depth++,node=node.parentElement){
        var buttons=node.querySelectorAll('button');
        var hasAdd=false;
        for(var b=0;b<buttons.length;b++) if(/add photos|camera/i.test(buttons[b].textContent||'')) hasAdd=true;
        if(hasAdd || /drop|upload/i.test(node.className||'')){node.style.setProperty('display','none','important');break;}
      }
    }
    document.body.classList.add('dusk-has-photos');
  }
  function findButton(re){
    var bs=document.querySelectorAll('button,[role="button"]');
    for(var i=0;i<bs.length;i++) if(re.test((bs[i].textContent||'').trim())) return bs[i];
    return null;
  }
  function downloadFallback(){
    var c=document.getElementById('work')||document.querySelector('.compare-pane canvas');
    if(!c || !c.toDataURL) return;
    var a=document.createElement('a');a.href=c.toDataURL('image/png');a.download='duskreel-edit.png';document.body.appendChild(a);a.click();a.remove();
  }
  function showPreviewFallback(){
    var existing=findButton(/^preview$/i);
    if(existing && existing.id!=='duskMobilePreview') {existing.click();return;}
    var c=document.getElementById('work')||document.querySelector('.compare-pane canvas');
    if(!c)return;
    var old=document.getElementById('duskPreviewModal');if(old)old.remove();
    var modal=document.createElement('div');modal.id='duskPreviewModal';
    modal.style.cssText='position:fixed;inset:0;z-index:99999;background:rgba(0,0,0,.92);display:flex;flex-direction:column;align-items:center;justify-content:center;padding:16px';
    var close=document.createElement('button');close.textContent='Close';close.style.cssText='position:absolute;right:14px;top:14px;padding:10px 16px;border:1px solid #555;border-radius:8px;background:#252525;color:#fff;font-weight:700';close.onclick=function(){modal.remove()};
    var copy=document.createElement('canvas');copy.width=c.width;copy.height=c.height;copy.getContext('2d').drawImage(c,0,0);
    copy.style.cssText='max-width:100%;max-height:82%;object-fit:contain;background:#111';modal.appendChild(copy);modal.appendChild(close);document.body.appendChild(modal);
  }
  function addActions(){
    if(innerWidth>760 || document.getElementById('duskMobileActions'))return;
    var bar=document.createElement('div');bar.id='duskMobileActions';
    var p=document.createElement('button');p.className='dusk-preview-btn';p.id='duskMobilePreview';p.textContent='Preview';
    var d=document.createElement('button');d.className='dusk-download-btn';d.id='duskMobileDownload';d.textContent='Download';
    p.onclick=function(){showPreviewFallback()};
    d.onclick=function(){var x=findButton(/download|export/i);if(x && x.id!=='duskMobileDownload')x.click();else downloadFallback()};
    bar.appendChild(p);bar.appendChild(d);
    var stage=document.querySelector('main .stage,main .clean-stage');
    if(stage && stage.parentElement) stage.parentElement.insertBefore(bar,stage.nextSibling);
    else document.querySelector('main')?.appendChild(bar);
  }
  function sync(){
    if(innerWidth>760)return;
    hideUploadCard();
    addActions();
    var ba=document.querySelector('.before-after');
    if(ba && hasLoadedPhoto()) ba.style.setProperty('display','flex','important');
  }
  function init(){
    sync();
    if(window.__duskV8)return;
    window.__duskV8=true;
    new MutationObserver(function(){sync()}).observe(document.body,{subtree:true,childList:true,attributes:true,attributeFilter:['style','class','src']});
    setInterval(sync,1000);
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();
})();
</script>
'''

s = s.replace('</head>', css + '\n</head>', 1)
s = s.replace('</body>', js + '\n</body>', 1)
p.write_text(s, encoding='utf-8')
print('Installed V8: clean mobile canvas, working preview/download, and PixelLab categories')
