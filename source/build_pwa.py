import hashlib, json, shutil, sys, os
src, out = sys.argv[1], sys.argv[2]
body = open(os.path.join(src,'index.html'), encoding='utf8').read()
q = open(os.path.join(src,'questions.json'), 'rb').read()
ver = hashlib.sha1(body.encode()+q).hexdigest()[:10]
head = '''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#2F4BD8">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="apple-mobile-web-app-title" content="Révision AMF">
<link rel="manifest" href="manifest.webmanifest">
<link rel="apple-touch-icon" href="icon-180.png">
<link rel="icon" href="icon-192.png">
<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>
</head>
<body>
'''
open(os.path.join(out,'index.html'),'w',encoding='utf8').write(head+body+'\n</body>\n</html>\n')
open(os.path.join(out,'questions.json'),'wb').write(q)
json.dump({"name":"Révision AMF","short_name":"AMF","lang":"fr","start_url":"./","scope":"./","display":"standalone",
  "background_color":"#F3F5F8","theme_color":"#2F4BD8",
  "icons":[{"src":"icon-192.png","sizes":"192x192","type":"image/png"},{"src":"icon-512.png","sizes":"512x512","type":"image/png"},{"src":"icon-512.png","sizes":"512x512","type":"image/png","purpose":"maskable"}]},
  open(os.path.join(out,'manifest.webmanifest'),'w',encoding='utf8'),ensure_ascii=False,indent=1)
sw = '''const CACHE="amf-%s";
const FILES=["./","index.html","questions.json","manifest.webmanifest","icon-180.png","icon-192.png","icon-512.png"];
self.addEventListener("install",e=>{e.waitUntil(caches.open(CACHE).then(c=>c.addAll(FILES)).then(()=>self.skipWaiting()))});
self.addEventListener("activate",e=>{e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k!==CACHE&&k!=="amf-fonts").map(k=>caches.delete(k)))).then(()=>self.clients.claim()))});
self.addEventListener("fetch",e=>{
  const u=new URL(e.request.url);
  if(e.request.method!=="GET")return;
  if(u.hostname==="fonts.googleapis.com"||u.hostname==="fonts.gstatic.com"){
    e.respondWith(caches.open("amf-fonts").then(c=>c.match(e.request).then(r=>r||fetch(e.request).then(res=>{c.put(e.request,res.clone());return res}).catch(()=>r))));return}
  if(u.origin!==location.origin)return;
  e.respondWith(caches.match(e.request,{ignoreSearch:true}).then(r=>r||fetch(e.request).catch(()=>caches.match("index.html"))));
});
''' % ver
open(os.path.join(out,'sw.js'),'w').write(sw)
print('version',ver)
