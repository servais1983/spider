import unittest
from src.crawler.static_crawler import StaticCrawler
from unittest.mock import patch, MagicMock

class TestStaticCrawler(unittest.TestCase):
    @patch('httpx.Client')
    def test_crawl_success(self, mock_client):
        # Setup mock
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = '<html><body><a href="/page1">Link 1</a><a href="https://example.com/page2">Link 2</a></body></html>'
        
        mock_session = MagicMock()
        mock_session.get.return_value = mock_response
        mock_client.return_value = mock_session
        
        # Test
        crawler = StaticCrawler("https://example.com")
        result = crawler.crawl()
        
        # Verify
        self.assertEqual(len(result), 2)
        self.assertIn("https://example.com/page1", result)
        self.assertIn("https://example.com/page2", result)
        
    @patch('httpx.Client')
    def test_crawl_failure(self, mock_client):
        # Setup mock for failure
        mock_session = MagicMock()
        mock_session.get.side_effect = Exception("Connection error")
        mock_client.return_value = mock_session
        
        # Test
        crawler = StaticCrawler("https://example.com")
        result = crawler.crawl()
        
        # Verify
        self.assertEqual(len(result), 0)

if __name__ == "__main__":
    unittest.main()
