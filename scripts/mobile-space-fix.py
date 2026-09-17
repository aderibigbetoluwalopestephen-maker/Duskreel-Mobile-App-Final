from pathlib import Path
import re

p = Path('index.html')
s = p.read_text(encoding='utf-8')

# Replace this small finalizer on every workflow run.
s = re.sub(r'<style[^>]*id=["\']duskreel-mobile-space-fix["\'][^>]*>.*?</style>\s*', '', s, flags=re.S|re.I)
s = re.sub(r'<script[^>]*id=["\']duskreel-mobile-space-fix-js["\'][^>]*>.*?</script>\s*', '', s, flags=re.S|re.I)

css = '''
<style id="duskreel-mobile-space-fix">
@media(max-width:760px){
  /* Do not leave a giant empty panel under the toolbar. Open it only when a category is tapped. */
  main .panel{display:none!important;flex:none!important;height:0!important;max-height:0!important;min-height:0!important;overflow:hidden!important;padding:0!important}
  main.dusk-panel-open .panel{display:block!important;flex:1 1 auto!important;height:auto!important;max-height:none!important;min-height:0!important;overflow-y:auto!important;padding:8px 9px 12px!important}
  #duskPixelDock{order:4!important}
}
</style>
'''

js = '''
<script id="duskreel-mobile-space-fix-js">
(function(){
  function init(){
    if(innerWidth>760)return;
    var main=document.querySelector('main'),dock=document.getElementById('duskPixelDock');
    if(!main||!dock||dock.dataset.spaceFix)return;
    dock.dataset.spaceFix='1';
    dock.querySelectorAll('.dpt-cat').forEach(function(cat){
      cat.addEventListener('click',function(){
        main.classList.add('dusk-panel-open');
        var map={adjust:'#expSlider',effects:'#fxGrid',crop:'#cropTools',ai:'#autoEditBtn',media:'#photoInput',export:'#exportAll',text:'#watermarkBtn',canvas:'#watermarkBtn'};
        var t=document.querySelector(map[cat.dataset.cat]);
        var panel=main.querySelector('.panel');
        if(t&&panel)setTimeout(function(){panel.scrollTo({top:Math.max(0,t.closest('.block')?.offsetTop||0),behavior:'smooth'});},30);
      });
    });
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();
})();
</script>
'''

s = s.replace('</head>', css + '</head>', 1)
s = s.replace('</body>', js + '</body>', 1)
p.write_text(s, encoding='utf-8')
print('Mobile spacing finalizer installed.')