#!/bin/bash
echo "[*] Installation Spider..."

# Mise à jour et installation des dépendances système
sudo apt update
sudo apt install -y python3 python3-pip

# Installation des dépendances Python
pip install -r requirements.txt

# Installation de Playwright et de Chromium
playwright install chromium

# Création des répertoires manquants
mkdir -p tests

# Rendre le script principal exécutable
chmod +x src/main.py

echo "[✓] Spider prêt. Exemple :"
echo "python src/main.py -u https://example.com -m sqli"
