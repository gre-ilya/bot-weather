import os
from dotenv import load_dotenv
import aiohttp

load_dotenv()
WEATHER_HEADERS = {'X-Yandex-API-Key': os.environ['WEATHER_API_KEY']}


async def get_weather(city: str):
    city = city.lower()
    if not city.isalpha():
        return 'Город не найден'
    return 'Город найден'
    # lon = 322
    # lang = 'ru_RU'
    # limit = 228
    # hours = 228
    # extra = 228
    # async with aiohttp.ClientSession() as session:
    #     url = f'https://api.gismeteo.net/v2/search/cities/?query={city}'
    #     async with session.get(url=url, headers=WEATHER_HEADERS) as res:
    #         print(res.status)
    #         print(res.text())
