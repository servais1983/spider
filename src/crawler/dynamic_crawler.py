from playwright.sync_api import sync_playwright

class DynamicCrawler:
    def __init__(self, base_url):
        self.base_url = base_url
        self.discovered_urls = set()
        
    def extract_links(self, page):
        """Extract links from a page rendered by Playwright"""
        all_links = page.query_selector_all('a')
        for link in all_links:
            href = link.get_attribute('href')
            if href:
                # Add to discovered URLs
                self.discovered_urls.add(href)
        return self.discovered_urls
        
    def crawl(self):
        """Crawl the target URL using headless browser"""
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            
            try:
                page.goto(self.base_url)
                
                # Wait for page to load completely
                page.wait_for_load_state('networkidle')
                
                # Extract links
                links = self.extract_links(page)
                
                browser.close()
                return links
                
            except Exception as e:
                print(f"Dynamic crawl failed: {e}")
                browser.close()
                return []
