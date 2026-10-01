from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import re
root=Path(__file__).parent/'dist'
errors=[]
class Page(HTMLParser):
 def __init__(self,path): super().__init__(); self.path=path; self.refs=[];self.ids=set();self.h1=0
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if tag=='h1':self.h1+=1
  if 'id' in a:
   if a['id'] in self.ids:errors.append(f'{self.path.name}: duplicate ID {a["id"]}')
   self.ids.add(a['id'])
  for k in ['href','src']:
   if k in a:self.refs.append(a[k])
  if tag=='img' and 'alt' not in a:errors.append(f'{self.path.name}: missing image alt')
pages={}
VERIFICATION=re.compile(r'^google[0-9a-f]{16}\.html$')  # Search Console ownership token, not a page
for path in root.glob('*.html'):
 if VERIFICATION.match(path.name):continue
 p=Page(path);p.feed(path.read_text(encoding='utf-8'));pages[path.name]=p
 if p.h1!=1:errors.append(f'{path.name}: expected one h1, found {p.h1}')
for name,p in pages.items():
 for ref in p.refs:
  u=urlsplit(ref)
  if u.scheme or u.netloc:continue
  target=(p.path.parent/unquote(u.path)) if u.path else p.path
  if not target.exists():errors.append(f'{name}: missing {ref}')
  if u.fragment and target.name in pages and u.fragment not in pages[target.name].ids:errors.append(f'{name}: missing anchor {ref}')
for css in (root/'assets/css').glob('experience.css'):
 for ref in re.findall(r'url\([\'"]?([^\)\'\"]+)',css.read_text(encoding='utf-8')):
  if not (css.parent/ref).exists():errors.append(f'{css.name}: missing {ref}')
assert not errors,'\n'.join(errors)
print(f'PASS: {len(pages)} pages, local links, fragment targets, image references, fonts, unique IDs and one main heading per page.')
print('Hero image KB:',round((root/'assets/brand/hero.webp').stat().st_size/1024),'mobile KB:',round((root/'assets/brand/hero-mobile.webp').stat().st_size/1024))
