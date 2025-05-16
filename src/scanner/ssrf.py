from src.utils.config_loader import load_payloads
import httpx
import re
from urllib.parse import urlparse, parse_qs

class SSRFScanner:
    def __init__(self, target_url):
        self.target_url = target_url
        # SSRF payloads typically point to internal resources or callback servers
        self.callback_server = "https://ssrftester.example.com"  # Replace with real callback server
        
    def scan(self):
        """Scan for SSRF vulnerabilities"""
        vulnerable = []
        base_url, _, query = self.target_url.partition('?')
        params = list(parse_qs(query).keys())
        
        # Generate unique callback URLs for each parameter
        for param in params:
            callback_url = f"{self.callback_server}/{param}"
            test_url = f"{base_url}?{param}={callback_url}"
            
            try:
                r = httpx.get(test_url, timeout=10)
                # In a real scenario, you would check your callback server logs
                # to see if it received a request from the target server
                
                # For demo purposes we're checking for common SSRF response patterns
                if self._check_ssrf_indicators(r):
                    vulnerable.append((test_url, callback_url))
            except Exception as e:
                # Timeout or connection errors might indicate potential SSRF
                # when server tries to connect to impossible destinations
                print(f"Error testing {test_url}: {e}")
                
        return vulnerable
        
    def _check_ssrf_indicators(self, response):
        """Check for indicators of SSRF vulnerability"""
        # Look for error patterns that might indicate SSRF attempts
        indicators = [
            "timeout",
            "connection refused",
            "unable to connect",
            "no route to host",
            "network is unreachable"
        ]
        
        # Check both response text and status code
        text_matches = any(ind in response.text.lower() for ind in indicators)
        
        # Status codes that might indicate connection problems on server side
        status_indicators = response.status_code in [500, 502, 504, 598]
        
        return text_matches or status_indicators
