![image](https://github.com/user-attachments/assets/3a1e3593-c539-474d-9951-3ffaa9f2e8b9)


# 🕷️ Spider – Bug Bounty Toolkit

Outil CLI modulaire pour pentesters et chasseurs de bug bounty.

## ⚙️ Installation

### Méthode 1: Installation rapide (recommandée)

```bash
# Cloner le dépôt
git clone https://github.com/servais1983/spider.git

# Accéder au répertoire du projet
cd spider

# Rendre le script d'installation exécutable
chmod +x install.sh

# Lancer l'installation
./install.sh

## 🔍 Fonctionnalités

* Crawl intelligent (statique et dynamique)
* Scan SQLi avec payloads personnalisés
* Rapport automatisé (Markdown)
* Mode furtif (rotation proxy, user-agent)

## 🚀 Exemple

```bash
python src/main.py -u https://example.com -m crawl
python src/main.py -u https://example.com?page=1 -m sqli
```

## 📋 Structure de projet

```
spider/
├── src/
│   ├── crawler/
│   │   ├── static_crawler.py
│   │   ├── dynamic_crawler.py
│   │   └── api_discovery.py
│   ├── scanner/
│   │   ├── sqli.py
│   │   ├── xss.py
│   │   └── ssrf.py
│   ├── utils/
│   │   ├── config_loader.py
│   │   ├── report_generator.py
│   │   └── stealth.py
│   └── main.py
├── config/
│   ├── config.yml
│   └── payloads/
│       ├── sqli.txt
│       └── xss.txt
├── tests/
├── requirements.txt
├── install.sh
└── README.md
```

## 📈 Roadmap

* Ajout du support XSS/CSRF
* Crawling dynamique avec Playwright
* Intégration avec OWASP ZAP/Nuclei
* Dashboard web (FastAPI + React)

## 🧰 Dépendances

* Python 3.7+
* httpx
* BeautifulSoup4
* Playwright (Chrome headless)
* PyYAML
* Free Proxies

## ⚠️ Avertissement

Cet outil est conçu uniquement pour un usage éthique dans le cadre de tests de sécurité autorisés. L'utilisateur est entièrement responsable de son utilisation et doit toujours obtenir les autorisations nécessaires avant de tester un système.

## 📄 Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.
