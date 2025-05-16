import argparse
from src.crawler.static_crawler import StaticCrawler
from src.scanner.sqli import SQLiScanner
from src.utils.report_generator import generate_report

def main():
    parser = argparse.ArgumentParser(description='Spider - Bug Bounty Toolkit')
    parser.add_argument('-u', '--url', required=True, help='Target URL')
    parser.add_argument('-m', '--module', choices=['crawl','sqli'], default='crawl')
    args = parser.parse_args()

    if args.module == 'crawl':
        crawler = StaticCrawler(args.url)
        urls = crawler.crawl()
        print(f"[+] Discovered URLs: {urls}")
    elif args.module == 'sqli':
        scanner = SQLiScanner(args.url)
        results = scanner.scan()
        if results:
            print(f"[!] SQLi Found:\n{results}")
            generate_report([{"type": "SQLi", "url": r[0], "payload": r[1]} for r in results])
        else:
            print("[✓] Aucun vecteur SQLi détecté.")

if __name__ == "__main__":
    main()
