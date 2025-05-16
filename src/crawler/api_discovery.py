import httpx
import json
import re
from urllib.parse import urlparse, urljoin

class ApiDiscovery:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = httpx.Client()
        self.discovered_apis = set()
        
    def extract_api_endpoints(self, html_content):
        """Extract potential API endpoints from HTML/JS content"""
        # Look for API endpoints in JavaScript
        api_patterns = [
            r'\/api\/[a-zA-Z0-9\/_-]+',  # /api/resource
            r'\/v[0-9]+\/[a-zA-Z0-9\/_-]+',  # /v1/resource
            r'\/rest\/[a-zA-Z0-9\/_-]+',  # /rest/resource
            r'url:\s*[\'"]([^\'"]+)[\'"]',  # url: '/endpoint'
            r'fetch\([\'"]([^\'"]+)[\'"]'  # fetch('/endpoint')
        ]
        
        for pattern in api_patterns:
            matches = re.findall(pattern, html_content)
            for match in matches:
                # Make relative URLs absolute
                if match.startswith('/'):
                    parsed_url = urlparse(self.base_url)
                    base = f"{parsed_url.scheme}://{parsed_url.netloc}"
                    endpoint = urljoin(base, match)
                else:
                    endpoint = match
                    
                self.discovered_apis.add(endpoint)
        
        return self.discovered_apis
        
    def find_swagger_docs(self):
        """Try to find Swagger/OpenAPI documentation"""
        common_swagger_paths = [
            '/swagger/index.html',
            '/api-docs',
            '/swagger-ui.html',
            '/swagger-ui',
            '/openapi.json',
            '/v1/api-docs',
            '/swagger'
        ]
        
        parsed_url = urlparse(self.base_url)
        base = f"{parsed_url.scheme}://{parsed_url.netloc}"
        
        for path in common_swagger_paths:
            try:
                url = urljoin(base, path)
                response = self.session.get(url, timeout=5)
                if response.status_code == 200:
                    content_type = response.headers.get('content-type', '')
                    if 'json' in content_type or 'yaml' in content_type or 'html' in content_type:
                        self.discovered_apis.add(url)
            except Exception:
                pass
        
    def discover(self):
        """Main method to discover APIs"""
        try:
            # Get the HTML content
            response = self.session.get(self.base_url)
            if response.status_code == 200:
                # Extract API endpoints from HTML/JS
                self.extract_api_endpoints(response.text)
                
                # Look for swagger docs
                self.find_swagger_docs()
                
                return self.discovered_apis
        except httpx.RequestError as e:
            print(f"API discovery failed: {e}")
        
        return []
