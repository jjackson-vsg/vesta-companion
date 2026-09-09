// Maintainer-only PDF build using an already installed Playwright.
const {chromium}=require("playwright");
const path=require("node:path"),fs=require("node:fs/promises");
const {pathToFileURL}=require("node:url");
(async()=>{
 const root=path.resolve(__dirname,"..");
 const browser=await chromium.launch({channel:"msedge",headless:true});
 try{
 const page=await browser.newPage({viewport:{width:1440,height:1100}});
 await page.goto(pathToFileURL(path.join(root,"START-HERE.html")).href);
 await page.emulateMedia({media:"print"});
 await page.locator("a[href]").evaluateAll(links=>links.forEach(a=>{const raw=a.getAttribute("href");if(raw && !/^(https?:|#)/.test(raw))a.href="https://github.com/jjackson-vsg/vesta-companion/blob/main/"+raw}));
 await page.pdf({path:path.join(root,"docs/Quick-start.pdf"),format:"A4",printBackground:true,preferCSSPageSize:true,tagged:true,outline:true});
 await fs.mkdir(path.join(root,".work/qa"),{recursive:true});
 const layout=await page.locator(".page").evaluateAll(pages=>pages.map((p,i)=>({page:i+1,height:p.getBoundingClientRect().height,overflow:getComputedStyle(p).overflow!=="hidden" && p.scrollHeight>p.clientHeight+2,lastContentBottom:p.querySelector(".page-foot").previousElementSibling.getBoundingClientRect().bottom-p.getBoundingClientRect().top,footerTop:p.querySelector(".page-foot").getBoundingClientRect().top-p.getBoundingClientRect().top})));
 await fs.writeFile(path.join(root,".work/qa/guide-layout.json"),JSON.stringify(layout,null,2));
 if(layout.some(x=>x.overflow||x.lastContentBottom>x.footerTop-12))throw Error("Guide content overlaps page/footer; inspect .work/qa/guide-layout.json");
 await page.emulateMedia({media:"screen"});
 await page.screenshot({path:path.join(root,".work/qa/guide-cover.png")});
 console.log("Created docs/Quick-start.pdf; page layout checked:",layout.length);
 }finally{await browser.close()}
})().catch(e=>{console.error(e.message);process.exitCode=1});
