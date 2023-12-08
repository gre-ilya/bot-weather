import os
from dotenv import load_dotenv
from handlers.start import start
from handlers.weather import weather

import logging
from telegram.ext import ApplicationBuilder, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

if __name__ == '__main__':
    load_dotenv()
    bot_token = os.environ['BOT_TOKEN']
    application = ApplicationBuilder().token(bot_token).build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('weather', weather))
    application.run_polling()
