import os
import asyncio
from playwright.async_api import async_playwright
from .config import TIMEOUT, DEFAULT_VIEWPORT, MOBILE_VIEWPORT
from .extractors import extract_metadata
from .storage import get_screenshot_path

async def run_audit(url: str, run_id: str, run_path: str, is_mobile: bool = False):
    async with async_playwright() as p:
        browser = await p.chromium.launch(args=["--no-sandbox", "--disable-gpu", "--disable-dev-shm-usage"])
        context = await browser.new_context(
            viewport=MOBILE_VIEWPORT if is_mobile else DEFAULT_VIEWPORT,
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
        )
        
        page = await context.new_page()
        console_logs = []
        network_failures = []
        
        # Robust log capture via init script
        await context.add_init_script("""
            window.__REDTEAM_LOGS = [];
            const hijack = (type) => {
                const original = console[type];
                console[type] = (...args) => {
                    const msg = args.map(a => typeof a === 'object' ? JSON.stringify(a) : String(a)).join(' ');
                    window.__REDTEAM_LOGS.push(`[${type}] ${msg}`);
                    original.apply(console, args);
                };
            };
            hijack('log'); hijack('error'); hijack('warn');
        """)

        page.on("console", lambda msg: console_logs.append(f"[{msg.type}] {msg.text}"))
        page.on("pageerror", lambda exc: console_logs.append(f"[exception] {exc}"))
        page.on("requestfailed", lambda req: network_failures.append(f"{req.method} {req.url} - {req.failure.error_text}"))
        
        try:
            await page.goto(url, wait_until="load", timeout=TIMEOUT)
            await asyncio.sleep(2)
            
            # Autonomous discovery and interaction
            elements = await page.query_selector_all("button, a")
            for btn in elements[:8]:
                try:
                    await btn.click(timeout=1500)
                    await asyncio.sleep(1)
                except: continue
        except Exception as e:
            print(f"Audit warning: {e}")

        # Final data collection
        extra_logs = await page.evaluate("window.__REDTEAM_LOGS || []")
        console_logs.extend(extra_logs)
        unique_logs = list(dict.fromkeys(console_logs))
        
        screenshot_filename = "main_page.png"
        await page.screenshot(path=os.path.join(run_path, "screenshots", screenshot_filename), full_page=True)
        
        content = await page.content()
        headings, extracted_elements = extract_metadata(content)
        title = await page.title()
        
        await browser.close()
        
        return {
            "run_id": run_id,
            "url": url,
            "title": title,
            "screenshot_path": get_screenshot_path(run_id, screenshot_filename),
            "console_logs": unique_logs,
            "network_failures": network_failures,
            "important_elements": extracted_elements,
            "headings": headings
        }
