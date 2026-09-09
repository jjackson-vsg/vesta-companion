// Real offline browser tests against fictional task data only.
const {chromium}=require("playwright"),assert=require("node:assert/strict");
const fs=require("node:fs/promises"),path=require("node:path"),{pathToFileURL}=require("node:url"),crypto=require("node:crypto");
(async()=>{
 const root=path.resolve(__dirname,".."),qa=path.join(root,".work/qa");await fs.mkdir(qa,{recursive:true});
 const browser=await chromium.launch({channel:"msedge",headless:true});
 try{
 const page=await browser.newPage({acceptDownloads:true,viewport:{width:1440,height:1050}});
 const errors=[],requests=[];page.on("pageerror",e=>errors.push(e.message));page.on("request",r=>{if(/^https?:/.test(r.url()))requests.push(r.url())});
 await page.goto(pathToFileURL(path.join(root,"examples/board.html")).href);
 assert.equal(await page.locator(".task").count(),3);
 await page.screenshot({path:path.join(root,"docs/assets/board-preview.png")});
 await page.getByRole("button",{name:"Completed",exact:true}).click();
 assert.equal(await page.locator(".task").count(),1);
 await page.getByRole("button",{name:"My priorities",exact:true}).click();
 await page.getByRole("button",{name:"+ Add a task",exact:true}).click();
 await page.locator("#f-title").fill('Review <script>window.pwned=true</script>');
 await page.locator("#f-project").fill("Fictional test");
 await page.locator("#f-due").fill("2026-12-01");
 await page.getByRole("button",{name:"Apply to board",exact:true}).click();
 assert.equal(await page.locator(".task").count(),4);
 assert.equal(await page.evaluate(()=>window.pwned),undefined);
 assert.equal(await page.locator("#save-title").textContent(),"Unsaved changes");
 assert.equal(await page.locator("#save").isDisabled(),true);
 await page.locator("#search").fill("Review <script>");
 assert.equal(await page.locator(".task").count(),1);
 await page.locator(".task input[type=checkbox]").click();
 assert.equal(await page.locator(".task").count(),0);
 await page.getByRole("button",{name:"Completed",exact:true}).click();
 assert.equal(await page.locator(".task").count(),1);
 const download=page.waitForEvent("download");await page.locator("#export").click();const file=await download;await file.saveAs(path.join(qa,"browser-export.json"));
 const exported=JSON.parse(await fs.readFile(path.join(qa,"browser-export.json"),"utf8"));
 assert.equal(exported.format,"companion-task-edit");
 assert.equal(exported.tasks.find(t=>t.project==="Fictional test").status,"done");
 assert.match(await page.locator("#notice").textContent(),/NOT updated/);
 await page.locator("#search").fill("");await page.getByRole("button",{name:"My priorities",exact:true}).click();
 await page.screenshot({path:path.join(qa,"board-desktop.png")});
 await page.setViewportSize({width:390,height:844});
 assert.equal(await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth),false);
 await page.screenshot({path:path.join(qa,"board-mobile.png"),fullPage:true});
 // Reload demo for direct-save and conflict tests. Stub only the OS file picker/handle,
 // while exercising the actual application code, hashing, validation and write flow.
 await page.reload();
 const raw=await fs.readFile(path.join(root,"examples/tasks.json"),"utf8");
 await page.evaluate(raw=>{
 window.mockRaw=raw;window.mockWrites=0;
 window.showOpenFilePicker=async()=>[{name:"tasks.json",getFile:async()=>new File([window.mockRaw],"tasks.json",{type:"application/json"}),createWritable:async()=>({write:async text=>{window.mockNext=text;window.mockWrites++},close:async()=>{window.mockRaw=window.mockNext},abort:async()=>{}})}];
 },raw);
 await page.locator("#open-file").click();
 await page.waitForFunction(()=>document.getElementById("save-title").textContent==="Task file connected");
 await page.getByRole("button",{name:"Edit Prepare the weekly team update",exact:true}).click();
 await page.locator("#f-title").fill("Updated fictional task");
 await page.getByRole("button",{name:"Apply to board",exact:true}).click();
 // Delay the actual mock write so the saving state can be checked.
 await page.evaluate(()=>{
 const h=handle;
 const original=h.createWritable;
 h.createWritable=async()=>{const writer=await original();const write=writer.write;writer.write=async text=>{await new Promise(r=>{window.releaseMockWrite=r});await write(text)};return writer};
 });
 await page.locator("#save").click();
 assert.equal(await page.locator("#add").isDisabled(),true);
 assert.equal(await page.locator("#open-file").isDisabled(),true);
 assert.equal(await page.locator(".task button").first().isDisabled(),true);
 await page.waitForFunction(()=>typeof window.releaseMockWrite==="function");
 await page.evaluate(()=>window.releaseMockWrite());
 await page.waitForFunction(()=>document.getElementById("notice").textContent.includes("Saved to the selected"));
 assert.equal(JSON.parse(await page.evaluate(()=>window.mockRaw)).revision,1);
 await page.getByRole("button",{name:"Edit Updated fictional task",exact:true}).click();
 await page.locator("#f-notes").fill("An unsaved change");
 await page.getByRole("button",{name:"Apply to board",exact:true}).click();
 await page.evaluate(()=>window.mockRaw+=" ");
 await page.locator("#save").click();
 await page.waitForFunction(()=>document.getElementById("notice").textContent.includes("changed elsewhere"));
 assert.equal(await page.evaluate(()=>window.mockWrites),1);
 assert.equal(await page.locator("#save-title").textContent(),"Unsaved changes");
 // A BOM file retains byte-accurate hashes for cross-tool imports.
 await page.evaluate(raw=>{window.mockRaw="\uFEFF"+raw},raw);
 page.once("dialog",d=>d.accept());
 await page.locator("#open-file").click();
 await page.waitForFunction(()=>document.getElementById("save-title").textContent==="Task file connected");
 assert.equal(await page.evaluate(()=>baseHash),crypto.createHash("sha256").update("\uFEFF"+raw).digest("hex"));
 assert.equal(await page.evaluate(()=>{try{validate({...doc,unexpected:"field"});return false}catch{return true}}),true);
 assert.equal(await page.evaluate(()=>{try{serialise({text:"x".repeat(2000001)});return false}catch{return true}}),true);
 // Check guide page count and local links.
 const guide=await browser.newPage({viewport:{width:1440,height:1100}});
 await guide.goto(pathToFileURL(path.join(root,"START-HERE.html")).href);
 assert.equal(await guide.locator(".page").count(),12);
 await guide.setViewportSize({width:390,height:844});
 assert.equal(await guide.evaluate(()=>document.documentElement.scrollWidth>innerWidth),false);
 await guide.screenshot({path:path.join(qa,"guide-mobile.png"),fullPage:false});
 assert.deepEqual(errors,[]);assert.deepEqual(requests,[]);
 await fs.writeFile(path.join(qa,"browser-results.json"),JSON.stringify({result:"passed",checks:["filtering","adding","completion","XSS-safe display","export envelope","unsaved warnings","desktop/mobile layout","selected-file save/read-back via mocked OS handle","stale-source refusal","editing locked during save","byte-accurate BOM hashing","oversize save refusal","strict document fields","offline no HTTP requests","guide mobile layout"],limitations:["OS file picker permission UI mocked","no live agent or Microsoft 365 calls"]},null,2));
 console.log("PASS browser behaviour and responsive layout; no network requests. OS picker mocked.");
 }finally{await browser.close()}
})().catch(e=>{console.error(e);process.exitCode=1});
