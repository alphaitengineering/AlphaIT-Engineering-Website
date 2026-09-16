// Offline handler checks: no network requests or customer enquiries are sent.
import fs from 'node:fs';
import vm from 'node:vm';
import assert from 'node:assert/strict';
const code=fs.readFileSync(new URL('./dist/assets/js/experience.js',import.meta.url),'utf8');
for(const mode of ['success','rejected','network','invalid']) {
 let submit,reset=false,requests=0;
 const button={innerHTML:'Send your enquiry',disabled:false,textContent:''};
 const status={textContent:'',className:'',children:[],replaceChildren(...x){this.children=x;},append(...x){this.children.push(...x);}};
 const form={action:'https://api.web3forms.com/submit',reportValidity:()=>mode!=='invalid',querySelector:()=>button,reset:()=>{reset=true;},addEventListener:(event,fn)=>{if(event==='submit')submit=fn;}};
 const document={querySelector:()=>null,querySelectorAll:()=>[],addEventListener:()=>{},getElementById:id=>id==='projectForm'?form:id==='formStatus'?status:null,createTextNode:s=>s,createElement:()=>({})};
 const context={document,matchMedia:()=>({matches:true}),URLSearchParams,location:{search:''},FormData:class{},AbortSignal,fetch:async()=>{requests++;if(mode==='network')throw new Error('Offline');return{ok:mode==='success',json:async()=>({success:mode==='success'})};}};
 vm.runInNewContext(code,context);
 await submit({preventDefault(){}});
 assert.equal(button.disabled,false,mode+': button should be usable');
 if(mode==='invalid'){assert.equal(requests,0);assert.equal(reset,false);}
 else if(mode==='success'){assert.equal(reset,true);assert.equal(status.className,'ok');assert.match(status.textContent,/has been sent/);}
 else{assert.equal(reset,false);assert.equal(status.className,'err');assert(status.children.some(x=>x.href==='mailto:projects@alphaitengineering.com'));}
 console.log('PASS',mode);
}
