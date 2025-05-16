from src.utils.config_loader import load_payloads
import httpx
from urllib.parse import urlparse, parse_qs

class XSSScanner:
    def __init__(self, target_url):
        self.target_url = target_url
        self.payloads = load_payloads('xss')
        
    def scan(self):
        """Scan for XSS vulnerabilities"""
        vulnerable = []
        base_url, _, query = self.target_url.partition('?')
        params = list(parse_qs(query).keys())
        
        for param in params:
            for payload in self.payloads:
                test_url = f"{base_url}?{param}={payload}"
                try:
                    r = httpx.get(test_url)
                    if self._check_reflection(r, payload):
                        vulnerable.append((test_url, payload))
                except Exception as e:
                    print(f"Error testing {test_url}: {e}")
                    
        return vulnerable
        
    def _check_reflection(self, response, payload):
        """Check if the payload is reflected in the response"""
        # Basic check if the payload appears in the response
        if payload in response.text:
            # Look for modifications to the payload that might prevent execution
            # For example, if <script> becomes &lt;script&gt;, it's not vulnerable
            sanitized = payload.replace('<', '&lt;').replace('>', '&gt;')
            if sanitized in response.text and payload not in response.text:
                return False
            return True
        return False
