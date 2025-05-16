import httpx
from bs4 import BeautifulSoup
from urllib.parse import urljoin

class StaticCrawler:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = httpx.Client()
        self.discovered_urls = set()

    def extract_links(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        for link in soup.find_all('a', href=True):
            full_url = urljoin(self.base_url, link['href'])
            self.discovered_urls.add(full_url)
        return self.discovered_urls

    def crawl(self):
        try:
            response = self.session.get(self.base_url)
            if response.status_code == 200:
                return self.extract_links(response.text)
        except httpx.RequestError as e:
            print(f"Request failed: {e}")
        return []
