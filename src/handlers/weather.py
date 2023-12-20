from telegram import Update
from telegram.ext import ContextTypes
from services import cities


async def weather(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    city = await cities.parse_locality_name(update.message.text) # '/weather Прибрежный'
    if not city:
        return await context.bot.send_message(chat_id=update.effective_chat.id, text='Не правильный формат')
    settlements = await cities.get_settlements(city)
    if not settlements:
        return await context.bot.send_message(chat_id=update.effective_chat.id, text='Населённый пункт не найден')
    elif len(settlements) == 1:
        points = cities.parse_points(settlements[0])
        return await context.bot.send_message(chat_id=update.effective_chat.id, text=points)
    else:
        reply_text = ['Найдено несколько населённых пунктов, отправьте номер вашего:']
        for i in range(len(settlements)):
            reply_text.append(settlements[i]['GeoObject']['metaDataProperty']['GeocoderMetaData']['text'])
        return await context.bot.send_message(chat_id=update.effective_chat.id, text='\n'.join(reply_text))
