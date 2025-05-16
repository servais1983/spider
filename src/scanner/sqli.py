from src.utils.config_loader import load_payloads
import httpx
from urllib.parse import urlparse, parse_qs

class SQLiScanner:
    def __init__(self, target_url):
        self.target_url = target_url
        self.payloads = load_payloads('sqli')

    def scan(self):
        vulnerable = []
        base_url, _, query = self.target_url.partition('?')
        params = list(parse_qs(query).keys())
        for param in params:
            for payload in self.payloads:
                test_url = f"{base_url}?{param}={payload}"
                try:
                    r = httpx.get(test_url)
                    if self._is_vulnerable(r):
                        vulnerable.append((test_url, payload))
                except:
                    pass
        return vulnerable

    def _is_vulnerable(self, response):
        indicators = ['SQL syntax', 'mysql_fetch', 'ORA-', 'syntax error']
        return any(i in response.text for i in indicators)
