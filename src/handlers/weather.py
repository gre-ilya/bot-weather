from telegram import Update
from telegram.ext import ContextTypes
from services import cities


async def weather(update: Update, context: ContextTypes.DEFAULT_TYPE):
    city = await cities.parse_city_name(update.message.text)
    city_data = await cities.get_city_data(city)
    if not city_data:
        return await context.bot.send_message(chat_id=update.effective_chat.id, text='Город не найден')
    return await context.bot.send_message(chat_id=update.effective_chat.id, text=str(city_data))
