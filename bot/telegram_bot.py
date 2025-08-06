# telegram_bot.py
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

# 🔐 Récupération du token depuis une variable d'environnement
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# 🛠️ Configuration du logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# 📌 Commande /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Bienvenue sur LuckyJet Secure Alert Bot 🚀")

# 🚀 Lancement de l'application
def main():
    if not TOKEN:
        logger.error("Le token Telegram n'est pas défini. Vérifie TELEGRAM_BOT_TOKEN.")
        return

    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    logger.info("Bot lancé avec succès.")
    app.run_polling()

if __name__ == "__main__":
    main()
