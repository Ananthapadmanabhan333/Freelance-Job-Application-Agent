import asyncio
from playwright.async_api import async_playwright
from playwright_stealth import stealth_async
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DiscoveryAgent:
    def __init__(self, headless=True):
        self.headless = headless

    async def scan_upwork(self, keyword: str):
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=self.headless)
            context = await browser.new_context(
                user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
            )
            page = await context.new_page()
            await stealth_async(page)
            
            logger.info(f"Scanning Upwork for {keyword}...")
            url = f"https://www.upwork.com/nx/search/jobs/?q={keyword}&sort=recency"
            
            try:
                await page.goto(url, wait_until="networkidle", timeout=60000)
                # Wait for job cards to load
                await page.wait_for_selector('section[data-test="job-tile-list"]', timeout=30000)
                
                jobs = []
                job_tiles = await page.query_selector_all('section[data-test="job-tile-list"] > article')
                
                for tile in job_tiles[:10]:
                    title_elem = await tile.query_selector('h2.job-tile-title')
                    desc_elem = await tile.query_selector('span[data-test="job-description-text"]')
                    budget_elem = await tile.query_selector('span[data-test="budget"]')
                    
                    title = await title_elem.inner_text() if title_elem else "N/A"
                    description = await desc_elem.inner_text() if desc_elem else "N/A"
                    budget = await budget_elem.inner_text() if budget_elem else "N/A"
                    
                    jobs.append({
                        "title": title.strip(),
                        "description": description.strip(),
                        "budget": budget.strip(),
                        "platform": "Upwork"
                    })
                
                logger.info(f"Successfully discovered {len(jobs)} jobs on Upwork.")
                return jobs
            except Exception as e:
                logger.error(f"Error scanning Upwork: {e}")
                await page.screenshot(path="error_upwork.png")
                return []
            finally:
                await browser.close()

if __name__ == "__main__":
    agent = DiscoveryAgent(headless=False)
    asyncio.run(agent.scan_upwork("AI Agent"))
