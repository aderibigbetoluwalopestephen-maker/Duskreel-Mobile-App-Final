from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')
marker = 'DUSKREEL-MOBILE-CANVAS-UPLOAD-FIX-V4'
if marker in s:
    print('Mobile canvas/upload fix already installed')
    raise SystemExit(0)

css = r'''
/* DUSKREEL-MOBILE-CANVAS-UPLOAD-FIX-V4 */
@media (max-width:800px){
  body{overflow:hidden!important}
  #app{height:100dvh!important}
  main{display:block!important;position:relative!important;height:calc(100dvh - 52px)!important;overflow:hidden!important}
  main .rail,main .panel{display:none!important}
  main .stage{
    position:absolute!important;left:0!important;right:0!important;top:0!important;bottom:112px!important;
    padding:8px!important;margin:0!important;display:flex!important;align-items:center!important;justify-content:center!important;
    overflow:hidden!important;background:#080808!important;
  }
  canvas#work{max-width:100%!important;max-height:100%!important;width:auto!important;height:auto!important;object-fit:contain!important}
  /* Hide the original upload/drop card once a photo has been loaded. */
  body.dusk-has-photos #dropZone,
  body.dusk-has-photos .drop-zone,
  body.dusk-has-photos .upload-zone,
  body.dusk-has-photos [class*="drop-zone"],
  body.dusk-has-photos [class*="upload-zone"]{display:none!important}
  /* Two equal before/after panes under the header and above the tool dock. */
  #duskBeforeAfter{position:absolute;inset:8px;z-index:7;display:none;background:#050505;border-radius:8px;overflow:hidden}
  body.dusk-has-photos #duskBeforeAfter{display:flex}
  #duskBeforeAfter .dba-pane{position:relative;flex:1 1 50%;width:50%;min-width:0;display:flex;align-items:center;justify-content:center;overflow:hidden;background:#080808}
  #duskBeforeAfter .dba-pane+.dba-pane{border-left:2px solid #080808}
  #duskBeforeAfter img{width:100%;height:100%;object-fit:contain;display:block}
  #duskBeforeAfter .dba-label{position:absolute;left:9px;top:9px;padding:5px 8px;border-radius:5px;background:#000c;color:#fff;font-size:11px;font-weight:700;z-index:2}
  #duskPixelDock{height:112px!important}
  #duskPixelTools{height:64px!important}
  .dpt-categories{height:48px!important}
  .export-bar{display:none!important}
}
@media (min-width:801px){#duskBeforeAfter{display:none!important}}
'''

html = r'''
<!-- DUSKREEL-MOBILE-CANVAS-UPLOAD-FIX-V4 -->
<div id="duskBeforeAfter" aria-label="Before and after preview">
  <div class="dba-pane"><span class="dba-label">Before</span><img id="duskBeforeImg" alt="Before preview"></div>
  <div class="dba-pane"><span class="dba-label">After</span><img id="duskAfterImg" alt="After preview"></div>
</div>
<script>
(function(){
  function isRealPhoto(img){return img && img.tagName==='IMG' && img.naturalWidth>0 && img.src && !img.closest('#authScreen') && !img.closest('#duskBeforeAfter')}
  function findPhoto(){
    var imgs=document.querySelectorAll('main img');
    for(var i=0;i<imgs.length;i++) if(isRealPhoto(imgs[i])) return imgs[i];
    return null;
  }
  function sync(){
    var img=findPhoto();
    var before=document.getElementById('duskBeforeImg'),after=document.getElementById('duskAfterImg');
    if(!before||!after)return;
    var loaded=!!img;
    if(img){before.src=img.src;after.src=img.src}
    document.body.classList.toggle('dusk-has-photos',loaded);
  }
  function hideUpload(){
    var text=(document.body.innerText||'').toLowerCase();
    var loaded=/\b\d+\s+photos?\s+loaded\b/.test(text) || !!findPhoto();
    document.body.classList.toggle('dusk-has-photos',loaded);
  }
  function init(){
    var stage=document.querySelector('main .stage');
    if(!stage)return;
    if(!document.getElementById('duskBeforeAfter')){
      var wrap=document.createElement('div');wrap.id='duskBeforeAfter';
      wrap.innerHTML='<div class="dba-pane"><span class="dba-label">Before</span><img id="duskBeforeImg" alt="Before preview"></div><div class="dba-pane"><span class="dba-label">After</span><img id="duskAfterImg" alt="After preview"></div>';
      stage.appendChild(wrap);
    }
    sync();hideUpload();
    var observer=new MutationObserver(function(){sync();hideUpload()});
    observer.observe(document.body,{subtree:true,childList:true,attributes:true,attributeFilter:['src','class','style']});
    setInterval(function(){sync();hideUpload()},800);
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();
})();
</script>
'''

s = s.replace('</head>', css + '\n</head>', 1)
s = s.replace('</body>', html + '\n</body>', 1)
p.write_text(s, encoding='utf-8')
print('Mobile canvas/upload fix installed')
