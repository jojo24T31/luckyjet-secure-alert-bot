# luckyjet_scraper.py
import requests
from bs4 import BeautifulSoup

def fetch_luckyjet_data(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")
        # Exemple fictif : chercher une div avec les données
        data_div = soup.find("div", class_="luckyjet-data")

        if data_div:
            return data_div.text.strip()
        else:
            return "Aucune donnée trouvée."

    except Exception as e:
        return f"Erreur lors du scraping : {e}"
