(() => {
  'use strict';
  const menu = document.querySelector('.menu-toggle');
  const nav = document.getElementById('main-nav');
  function setMenu(open) {
    menu?.setAttribute('aria-expanded', String(open));
    menu?.setAttribute('aria-label', open ? 'Close navigation' : 'Open navigation');
    nav?.classList.toggle('is-open', open);
  }
  menu?.addEventListener('click', () => setMenu(menu.getAttribute('aria-expanded') !== 'true'));
  document.addEventListener('keydown', e => { if (e.key === 'Escape' && menu?.getAttribute('aria-expanded') === 'true') {setMenu(false);menu.focus();} });
  document.addEventListener('click', e => {if (!e.target.closest('.header')) setMenu(false);});
  nav?.querySelectorAll('a').forEach(a => a.addEventListener('click', () => setMenu(false)));
  const reduced = matchMedia('(prefers-reduced-motion: reduce)');
  if (!reduced.matches && 'IntersectionObserver' in window) {
    document.documentElement.classList.add('js-motion');
    const observer = new IntersectionObserver(entries => entries.forEach(entry => {if(entry.isIntersecting){entry.target.classList.add('seen');observer.unobserve(entry.target);}}),{threshold:.08});
    document.querySelectorAll('.section-head,.product-card,.delivery-steps article,.workflow-columns article').forEach(el => {el.classList.add('reveal');observer.observe(el);});
  }
  const hero = document.querySelector('[data-hero]');
  if(hero && !reduced.matches && matchMedia('(pointer:fine)').matches) {
    hero.addEventListener('pointermove', e => {
      const r = hero.getBoundingClientRect();
      hero.style.setProperty('--hero-x', `${(e.clientX-r.left-r.width/2)*.007}px`);
      hero.style.setProperty('--hero-y', `${(e.clientY-r.top-r.height/2)*.007}px`);
    },{passive:true});
    hero.addEventListener('pointerleave',()=>{hero.style.setProperty('--hero-x','0px');hero.style.setProperty('--hero-y','0px');});
  }
  const routes = [
    {name:'Varren',short:'Varren',icon:'varren-mark.png',url:'varren.html',field:['Create new revenue','Qualified opportunities'],summary:'Varren finds the strongest commercial route, carries out approved work and improves the next move from real results.',accent:'#6E1028',glow:'#B89A68'},
    {name:'Verdika',short:'Verdika',icon:'verdika-mark.png',url:'verdika.html',field:['Improve the service','Accountable action'],summary:'Verdika turns people’s experience into clear patterns, puts the finding in front of the responsible team and shows what changes next.',accent:'#16245B',glow:'#D9A62E'},
    {name:'LisBon Trust Infrastructure (LTI)',short:'LSI + LTI',icon:'lisbon-icon.png',url:'lisbon-trust.html',field:['Trusted evidence','Controlled decision'],summary:'LSI validates the financial evidence. LTI turns it into a decision the institution can explain, control and replay.',accent:'#24198A',glow:'#C9A45C'}
  ];
  const tabs = [...document.querySelectorAll('[data-route]')];
  const panel = document.getElementById('route-panel');
  let routeIndex=0;
  let routeTimer=0;
  let routeVisible=false;
  let routePaused=false;
  const routeSection=document.querySelector('[data-route-section]');
  const pauseButton=document.querySelector('[data-route-pause]');
  const AUTO_DELAY=5500;
  const routeIcons=new Map();
  const routeIconsReady=Promise.all(routes.map(route=>new Promise(resolve=>{
    const image=new Image();
    image.onload=image.onerror=()=>resolve();
    image.src='assets/products/'+route.icon;
    routeIcons.set(route.icon,image);
  })));
  function stopAutoplay(){clearTimeout(routeTimer);routeTimer=0;}
  function scheduleAutoplay(delay=AUTO_DELAY){
    stopAutoplay();
    if(!routeVisible||routePaused||reduced.matches||document.hidden||tabs.length<2)return;
    routeTimer=setTimeout(()=>{selectRoute((routeIndex+1)%tabs.length);scheduleAutoplay();},delay);
  }
  function selectRoute(i, focus=false, manual=false){
    const route=routes[i];
    if(!route||!panel||!tabs.length)return;
    routeIndex=i;
    tabs.forEach((t,j)=>{t.setAttribute('aria-selected',String(i===j));t.tabIndex=i===j?0:-1;});
    const icon=document.querySelector('[data-route-icon]');
    if(icon){
      const prepared=routeIcons.get(route.icon);
      icon.src=prepared?.complete&&prepared.naturalWidth?prepared.src:'assets/products/'+route.icon;
      icon.closest('.field-core')?.classList.toggle('is-lisbon',route.short==='LSI + LTI');
    }
    const link=document.querySelector('[data-route-link]');if(link){link.href=route.url;link.textContent='Explore '+route.name+' ↗';}
    const product=document.querySelector('[data-field-product]');if(product)product.textContent=route.short;
    const storyLabel=document.querySelector('[data-route-story-label]');if(storyLabel)storyLabel.textContent=route.short+' in action';
    const summary=document.querySelector('[data-route-summary]');if(summary)summary.textContent=route.summary;
    document.querySelectorAll('[data-field-label]').forEach((el,j)=>el.textContent=route.field[j]);
    panel.style.setProperty('--route-accent',route.accent);
    panel.style.setProperty('--route-glow',route.glow);
    panel.setAttribute('aria-labelledby',tabs[i].id);
    panel.classList.remove('is-changing');void panel.offsetWidth;panel.classList.add('is-changing');
    if(focus)tabs[i].focus();
    if(manual)scheduleAutoplay(AUTO_DELAY*1.5);
  }
  tabs.forEach((t,i)=>{t.addEventListener('click',()=>selectRoute(i,false,true));t.addEventListener('keydown',e=>{let n=i;if(e.key==='ArrowRight')n=(i+1)%tabs.length;else if(e.key==='ArrowLeft')n=(i+tabs.length-1)%tabs.length;else if(e.key==='Home')n=0;else if(e.key==='End')n=tabs.length-1;else return;e.preventDefault();selectRoute(n,true,true);});});
  if(routeSection&&'IntersectionObserver' in window){
    new IntersectionObserver(([entry])=>{routeVisible=entry.isIntersecting&&entry.intersectionRatio>=.35;if(routeVisible)scheduleAutoplay();else stopAutoplay();},{threshold:[0,.35,.75]}).observe(routeSection);
    routeSection.addEventListener('focusin',stopAutoplay);
    routeSection.addEventListener('focusout',e=>{if(!routeSection.contains(e.relatedTarget))scheduleAutoplay();});
  }
  pauseButton?.addEventListener('click',()=>{routePaused=!routePaused;routeSection?.classList.toggle('is-paused',routePaused);pauseButton.setAttribute('aria-pressed',String(routePaused));pauseButton.textContent=routePaused?'Resume automatic preview':'Pause automatic preview';if(routePaused)stopAutoplay();else scheduleAutoplay();});
  document.addEventListener('visibilitychange',()=>{if(document.hidden)stopAutoplay();else scheduleAutoplay();});
  if(panel&&tabs.length)routeIconsReady.then(()=>selectRoute(0));
  const field=document.querySelector('.operating-field');
  if(field && !reduced.matches && matchMedia('(pointer:fine)').matches){
    field.addEventListener('pointermove',e=>{
      const r=field.getBoundingClientRect();
      const x=(e.clientX-r.left)/r.width-.5;
      const y=(e.clientY-r.top)/r.height-.5;
      field.style.transform=`rotateX(${(-y*4.5).toFixed(2)}deg) rotateY(${(x*6).toFixed(2)}deg) translateZ(0)`;
    },{passive:true});
    field.addEventListener('pointerleave',()=>{field.style.transform='rotateX(0deg) rotateY(0deg)';});
  }
  const form=document.getElementById('projectForm'),status=document.getElementById('formStatus');
  const interest=document.getElementById('interest');
  const selected=new URLSearchParams(location.search).get('product');
  if(interest && [...interest.options].some(o=>o.value===selected))interest.value=selected;
  form?.addEventListener('submit',async e=>{
    e.preventDefault();if(!form.reportValidity())return;
    const button=form.querySelector('[type=submit]');const label=button.innerHTML;
    button.disabled=true;button.textContent='Sending…';status.textContent='';status.className='';
    try{
      const response=await fetch(form.action,{method:'POST',headers:{Accept:'application/json'},body:new FormData(form),signal:AbortSignal.timeout(20000)});
      const data=await response.json();
      if(!response.ok||data.success!==true)throw new Error('Submission not confirmed');
      form.reset();status.className='ok';status.textContent='Thank you. Your enquiry has been sent to AlphaIT. We will be in touch.';
    }catch(err){status.className='err';status.replaceChildren(document.createTextNode('We could not confirm delivery. Please email '));const a=document.createElement('a');a.href='mailto:projects@alphaitengineering.com';a.textContent='projects@alphaitengineering.com';status.append(a,document.createTextNode(' or message us on WhatsApp.'));}
    finally{button.disabled=false;button.innerHTML=label;}
  });
})();
