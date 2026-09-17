from pathlib import Path
import re

path = Path('index.html')
text = path.read_text(encoding='utf-8')

# Remove an older copy if the workflow is run more than once.
text = re.sub(r'<style[^>]*id=["\']duskreel-mobile-download-menu["\'][^>]*>.*?</style>\s*', '', text, flags=re.S | re.I)
text = re.sub(r'<script[^>]*id=["\']duskreel-mobile-download-menu-js["\'][^>]*>.*?</script>\s*', '', text, flags=re.S | re.I)

css = r'''
<style id="duskreel-mobile-download-menu">
/* DUSKREEL MOBILE DOWNLOAD DROPDOWN */
@media(max-width:760px){
  header{position:relative!important;z-index:120!important}
  header .dusk-download-wrap{display:flex!important;align-items:center!important;position:relative!important;margin-left:7px!important}
  header .dusk-download-trigger{height:32px!important;min-width:76px!important;padding:0 10px!important;border:1px solid #4a2a52!important;border-radius:8px!important;background:#211425!important;color:#fff!important;font-size:10px!important;font-weight:800!important;display:flex!important;align-items:center!important;justify-content:center!important;gap:5px!important;cursor:pointer!important;touch-action:manipulation!important}
  header .dusk-download-trigger:active{transform:scale(.98)!important}
  header .dusk-download-chevron{font-size:9px!important;opacity:.8!important}
  header .dusk-download-popover{display:none!important;position:absolute!important;right:0!important;top:38px!important;width:160px!important;padding:6px!important;border:1px solid #4a2a52!important;border-radius:10px!important;background:#1e1220!important;box-shadow:0 14px 34px rgba(0,0,0,.55)!important;z-index:500!important}
  header .dusk-download-popover.open{display:block!important}
  header .dusk-download-popover button{display:flex!important;align-items:center!important;width:100%!important;min-height:40px!important;padding:8px 10px!important;border:0!important;border-radius:7px!important;background:transparent!important;color:#fff!important;text-align:left!important;font-size:11px!important;font-weight:700!important;cursor:pointer!important}
  header .dusk-download-popover button:hover{background:#2a1830!important}
  header .dusk-download-popover button strong{margin-left:auto!important;color:#cba6d1!important;font-size:9px!important;font-weight:600!important}
  #duskMobileActions{display:none!important}
}
@media(min-width:761px){header .dusk-download-wrap{display:none!important}}
</style>
'''

js = r'''
<script id="duskreel-mobile-download-menu-js">
(function(){
  function mobile(){return window.innerWidth<=760;}
  function findLogout(){
    var buttons=document.querySelectorAll('header button');
    for(var i=0;i<buttons.length;i++){
      var t=(buttons[i].textContent||'').trim().toLowerCase();
      if(t==='logout'||t.indexOf('logout')===0)return buttons[i];
    }
    return null;
  }
  function callAction(selector){
    var b=document.querySelector(selector);
    if(b){b.click();return true;}
    return false;
  }
  function install(){
    if(!mobile())return;
    var logout=findLogout();
    if(!logout)return;
    if(document.querySelector('header .dusk-download-wrap'))return;

    var wrap=document.createElement('div');
    wrap.className='dusk-download-wrap';
    wrap.innerHTML='<button type="button" class="dusk-download-trigger" aria-haspopup="menu" aria-expanded="false">Download <span class="dusk-download-chevron">▾</span></button>'+
      '<div class="dusk-download-popover" role="menu">'+
      '<button type="button" data-download-action="preview">Preview <strong>VIEW</strong></button>'+
      '<button type="button" data-download-action="download">Download <strong>SAVE</strong></button>'+
      '</div>';

    logout.parentNode.insertBefore(wrap,logout);
    var trigger=wrap.querySelector('.dusk-download-trigger');
    var pop=wrap.querySelector('.dusk-download-popover');
    trigger.addEventListener('click',function(e){
      e.preventDefault();e.stopPropagation();
      var open=pop.classList.toggle('open');
      trigger.setAttribute('aria-expanded',open?'true':'false');
    });
    pop.addEventListener('click',function(e){
      var b=e.target.closest('button');
      if(!b)return;
      e.preventDefault();e.stopPropagation();
      pop.classList.remove('open');
      trigger.setAttribute('aria-expanded','false');
      if(b.dataset.downloadAction==='preview')callAction('#duskMobileActions .dusk-preview-btn');
      if(b.dataset.downloadAction==='download')callAction('#duskMobileActions .dusk-download-btn');
    });
    document.addEventListener('click',function(e){
      if(!wrap.contains(e.target)){
        pop.classList.remove('open');
        trigger.setAttribute('aria-expanded','false');
      }
    });
  }
  function init(){install();setTimeout(install,500);setTimeout(install,1500);}
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();
})();
</script>
'''

text = text.replace('</head>', css + '\n</head>', 1)
text = text.replace('</body>', js + '\n</body>', 1)
path.write_text(text, encoding='utf-8')
print('Mobile Download dropdown installed.')
