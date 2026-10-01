const { chromium } = require('/Users/kiprastinfavicius/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright');
const fs = require('fs');
const path = require('path');
const root = __dirname;
(async () => {
  const browser = await chromium.launch({headless:true,executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'});
  const checks=[];
  for(const stripped of [false,true]) {
    for(const width of [600,390,320]) {
      const page=await browser.newPage({viewport:{width,height:900},deviceScaleFactor:1});
      await page.goto('file://'+path.join(root,'preview.html'));
      await page.evaluate(async()=>{await document.fonts.ready;await Promise.all([...document.images].map(i=>i.decode().catch(()=>{})));});
      if(stripped)await page.locator('style').evaluateAll(ss=>ss.forEach(s=>s.remove()));
      const info=await page.evaluate(()=>({
        width:innerWidth,scrollWidth:document.documentElement.scrollWidth,height:document.documentElement.scrollHeight,
        images:[...document.images].map(i=>({src:i.getAttribute('src'),loaded:i.complete&&i.naturalWidth>0,alt:!!i.alt})),
        descriptions:[...document.querySelectorAll('.product-description')].map(e=>({width:e.clientWidth,height:e.clientHeight,text:e.textContent})),
        overflow:[...document.body.querySelectorAll('*')].filter(e=>{const r=e.getBoundingClientRect();return r.width>0&&(r.right>innerWidth+1||r.left< -1)}).map(e=>({tag:e.tagName,text:e.textContent.slice(0,70)})),
        titleOverflow:[...document.querySelectorAll('h1,h2,h3')].filter(e=>e.scrollWidth>e.clientWidth+1).map(e=>e.textContent),
        links:[...document.querySelectorAll('a')].map(a=>a.getAttribute('href'))
      }));
      info.stripped=stripped;checks.push(info);
      const label=width===600?'desktop':width===390?'mobile':'mobile-320';
      await page.screenshot({path:path.join(root,`preview-${label}${stripped?'-no-style':''}.jpg`),type:'jpeg',quality:89,fullPage:true});
      if(width===390&&!stripped)await page.screenshot({path:path.join(root,'preview-mobile-top.jpg'),type:'jpeg',quality:89,fullPage:false});
      await page.close();
    }
  }
  await browser.close();
  fs.writeFileSync(path.join(root,'qa-results.json'),JSON.stringify(checks,null,2));
  for(const c of checks)console.log(JSON.stringify({width:c.width,stripped:c.stripped,height:c.height,scrollWidth:c.scrollWidth,loadedImages:c.images.filter(i=>i.loaded).length,images:c.images.length,descriptionWidths:c.descriptions.map(x=>x.width),descriptionHeights:c.descriptions.map(x=>x.height),overflow:c.overflow,titleOverflow:c.titleOverflow}));
  if(checks.some(c=>c.scrollWidth>c.width||c.overflow.length||c.titleOverflow.length||c.images.some(i=>!i.loaded||!i.alt)||c.descriptions.some(d=>d.width<244)))process.exitCode=1;
})();
