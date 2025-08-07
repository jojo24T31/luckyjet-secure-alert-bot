# alert_loop.py
# Ce fichier lance une boucle qui surveille les données Lucky Jet en continu.
# Si un événement critique est détecté (ex : multiplicateur élevé), une alerte est envoyée via Telegram.

import time
import os
import requests
from dotenv import load_dotenv
from bot.luckyjet_scraper import get_luckyjet_data

# Chargement des variables d'environnement
load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def check_for_alert(data, threshold=5.0):
    """Vérifie si le multiplicateur dépasse le seuil défini."""
    return data["multiplier"] >= threshold

def send_alert(message):
    """Envoie une alerte Telegram avec le message donné."""
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print(f"Erreur lors de l'envoi de l'alerte : {e}")

def run_alert_loop():
    """Boucle principale qui surveille les données et envoie des alertes."""
    while True:
        try:
            data = get_luckyjet_data()
            if check_for_alert(data):
                message = f"🚨 Alerte Lucky Jet !\nMultiplicateur détecté : {data['multiplier']}\nHeure : {data['timestamp']}"
                send_alert(message)
                print("Alerte envoyée.")
            else:
                print("Pas d'événement critique.")
        except Exception as e:
            print(f"Erreur dans la boucle : {e}")
        time.sleep(60)  # Vérifie toutes les 60 secondes

if __name__ == "__main__":
    run_alert_loop()
