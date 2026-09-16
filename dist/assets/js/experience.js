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
    {titles:['A business wants to create new revenue.','Varren operates the commercial mission.','Opportunities become visible and actionable.'],body:['It needs to find the right opportunity, decide where to focus and move the work forward.','It researches the market, recommends the route, coordinates approved work across tools and channels, then learns from the result.','Leaders see what happened, what worked, what should improve and which opportunity to pursue next.'],name:'Varren',short:'Varren',icon:'varren-mark.png',url:'varren.html',field:['Commercial objective','New opportunities'],accent:'#6f2438',glow:'#d8b46f'},
    {titles:['An organisation wants to improve a service.','Verdika turns experience into accountable action.','The right team can act and show what changed.'],body:['People are reporting problems and needs, but the signal is scattered and responsibility is unclear.','It structures feedback, reveals recurring patterns and directs the relevant finding to the responsible team.','Leaders see what people experienced, the response, the action and what people report afterwards.'],name:'Verdika',short:'Verdika',icon:'verdika-mark.png',url:'verdika.html',field:['Service experience','Clear action'],accent:'#315a9a',glow:'#7eb9ff'},
    {titles:['A lender needs to make a controlled credit decision.','LSI and LTI connect evidence to the decision.','The decision can be explained and replayed.'],body:['Raw financial records must become trusted evidence before policy can be applied.','LSI validates the financial evidence. LTI applies approved trust, eligibility, exposure and obligation rules.','The institution can inspect the evidence, rule, decision path, exposure and obligation state.'],name:'LisBon Trust Infrastructure (LTI)',short:'LSI + LTI',icon:'lisbon-icon.png',url:'lisbon-trust.html',field:['Financial evidence','Controlled decision'],accent:'#134f70',glow:'#73d4f4'}
  ];
  const tabs = [...document.querySelectorAll('[data-route]')];
  const panel = document.getElementById('route-panel');
  let routeIndex=0;
  let routeTimer=0;
  let routeVisible=false;
  let routePaused=false;
  const routeSection=document.querySelector('[data-route-section]');
  const pauseButton=document.querySelector('[data-route-pause]');
  const AUTO_DELAY=9000;
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
    document.querySelectorAll('[data-route-title]').forEach((el,j)=>el.textContent=route.titles[j]);
    document.querySelectorAll('[data-route-body]').forEach((el,j)=>el.textContent=route.body[j]);
    const icon=document.querySelector('[data-route-icon]');if(icon)icon.src='assets/products/'+route.icon;
    const link=document.querySelector('[data-route-link]');if(link){link.href=route.url;link.textContent='Explore '+route.name+' ↗';}
    const product=document.querySelector('[data-field-product]');if(product)product.textContent=route.short;
    document.querySelectorAll('[data-field-label]').forEach((el,j)=>el.textContent=route.field[j]);
    panel.style.setProperty('--route-accent',route.accent);
    panel.style.setProperty('--route-glow',route.glow);
    panel.setAttribute('aria-labelledby',tabs[i].id);
    panel.classList.remove('is-changing');void panel.offsetWidth;panel.classList.add('is-changing');
    if(focus)tabs[i].focus();
    if(manual)scheduleAutoplay(AUTO_DELAY*1.6);
  }
  tabs.forEach((t,i)=>{t.addEventListener('click',()=>selectRoute(i,false,true));t.addEventListener('keydown',e=>{let n=i;if(e.key==='ArrowRight')n=(i+1)%tabs.length;else if(e.key==='ArrowLeft')n=(i+tabs.length-1)%tabs.length;else if(e.key==='Home')n=0;else if(e.key==='End')n=tabs.length-1;else return;e.preventDefault();selectRoute(n,true,true);});});
  if(routeSection&&'IntersectionObserver' in window){
    new IntersectionObserver(([entry])=>{routeVisible=entry.isIntersecting&&entry.intersectionRatio>=.35;if(routeVisible)scheduleAutoplay();else stopAutoplay();},{threshold:[0,.35,.75]}).observe(routeSection);
    routeSection.addEventListener('pointerenter',stopAutoplay);
    routeSection.addEventListener('pointerleave',()=>scheduleAutoplay());
    routeSection.addEventListener('focusin',stopAutoplay);
    routeSection.addEventListener('focusout',e=>{if(!routeSection.contains(e.relatedTarget))scheduleAutoplay();});
  }
  pauseButton?.addEventListener('click',()=>{routePaused=!routePaused;pauseButton.setAttribute('aria-pressed',String(routePaused));pauseButton.textContent=routePaused?'Resume automatic preview':'Pause automatic preview';if(routePaused)stopAutoplay();else scheduleAutoplay();});
  document.addEventListener('visibilitychange',()=>{if(document.hidden)stopAutoplay();else scheduleAutoplay();});
  if(panel&&tabs.length)selectRoute(0);
  const field=document.querySelector('.operating-field');
  if(field && !reduced.matches && matchMedia('(pointer:fine)').matches){
    field.addEventListener('pointermove',e=>{
      const r=field.getBoundingClientRect();
      const x=(e.clientX-r.left)/r.width-.5;
      const y=(e.clientY-r.top)/r.height-.5;
      field.style.transform=`rotateX(${(-y*3).toFixed(2)}deg) rotateY(${(x*4).toFixed(2)}deg)`;
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
