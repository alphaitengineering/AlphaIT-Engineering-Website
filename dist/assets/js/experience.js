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
    document.querySelectorAll('.section-head,.product-card,.delivery-steps article,.workflow-columns article,.closing h2').forEach(el => {el.classList.add('reveal');observer.observe(el);});
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
    {titles:['A business wants to launch a service.','LFI provides the operating foundation.','The new service can operate.'],body:['The demand exists, but the operating system behind it does not.','Deploy route, job and execution infrastructure around the organisation’s brand and operation.','Teams can assign, run and evidence the work from one operating truth.'],name:'LisBon Flow Infrastructure (LFI)',short:'LFI',icon:'lfi-mark.png',url:'lisbon-flow.html',field:['Opportunity','New service']},
    {titles:['People keep reporting the same experience.','Verdika connects experience to responsibility.','The organisation can improve what matters.'],body:['Feedback exists across forms, messages and conversations, but the recurring pattern remains hidden.','Structure the contributions, reveal the pattern and put the finding in front of the responsible team.','Leaders can see the experience, response, action and what people report afterwards.'],name:'Verdika',short:'Verdika',icon:'verdika-mark.png',url:'verdika.html',field:['Experience','Visible improvement']},
    {titles:['A provider needs a controlled credit decision.','LSI and LTI connect evidence to policy.','The decision can be explained and replayed.'],body:['Raw financial records cannot safely move straight into a consequential decision.','Validate the records, produce governed signals and apply the authorised trust, eligibility and exposure rules.','The institution can inspect the evidence, applicable rule, decision path and obligation state.'],name:'LisBon Trust Infrastructure (LTI)',short:'LSI + LTI',icon:'lisbon-icon.png',url:'lisbon-trust.html',field:['Governed evidence','Trusted decision']}
  ];
  const tabs = [...document.querySelectorAll('[data-route]')];
  const panel = document.getElementById('route-panel');
  function selectRoute(i, focus=false){
    const route=routes[i];
    tabs.forEach((t,j)=>{t.setAttribute('aria-selected',String(i===j));t.tabIndex=i===j?0:-1;});
    document.querySelectorAll('[data-route-title]').forEach((el,j)=>el.textContent=route.titles[j]);
    document.querySelectorAll('[data-route-body]').forEach((el,j)=>el.textContent=route.body[j]);
    const icon=document.querySelector('[data-route-icon]');icon.src='assets/products/'+route.icon;
    const link=document.querySelector('[data-route-link]');link.href=route.url;link.textContent='Explore '+route.name+' ↗';
    const product=document.querySelector('[data-field-product]');if(product)product.textContent=route.short;
    document.querySelectorAll('[data-field-label]').forEach((el,j)=>el.textContent=route.field[j]);
    panel.setAttribute('aria-labelledby',tabs[i].id);
    panel.classList.remove('is-changing');void panel.offsetWidth;panel.classList.add('is-changing');
    if(focus)tabs[i].focus();
  }
  tabs.forEach((t,i)=>{t.addEventListener('click',()=>selectRoute(i));t.addEventListener('keydown',e=>{let n=i;if(e.key==='ArrowRight')n=(i+1)%tabs.length;else if(e.key==='ArrowLeft')n=(i+tabs.length-1)%tabs.length;else if(e.key==='Home')n=0;else if(e.key==='End')n=tabs.length-1;else return;e.preventDefault();selectRoute(n,true);});});
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
