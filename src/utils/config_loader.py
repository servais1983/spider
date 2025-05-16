import os

def load_payloads(vuln_type):
    file_path = os.path.join("config", "payloads", f"{vuln_type}.txt")
    with open(file_path, "r") as f:
        return [line.strip() for line in f if line.strip()]
