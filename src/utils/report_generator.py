from datetime import datetime

def generate_report(findings):
    filename = f"spider_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md"
    with open(filename, "w") as f:
        f.write("# Spider Security Report\n\n")
        for item in findings:
            f.write(f"## {item['type']} in {item['url']}\n")
            f.write(f"**Payload utilisé**: `{item['payload']}`\n\n")
    print(f"[✓] Rapport généré : {filename}")
