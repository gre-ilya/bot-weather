import os
import aiohttp
import json
from dotenv import load_dotenv


load_dotenv()
GEOCODE_API_KEY = os.environ['GEOCODE_API_KEY']


async def parse_city_name(text: str) -> str | None:
    words = text.split()
    if len(words) != 2:
        return None
    return words[1]


async def get_city_data(name: str):
    async with aiohttp.ClientSession() as session:
        params = {
            'apikey': GEOCODE_API_KEY,
            'geocode': name,
            'format': 'json'
        }
        async with session.get('https://geocode-maps.yandex.ru/1.x/', params=params) as res:
            res_json = await res.json()
            res_dict = dict(res_json)
            geo_objects = res_dict['response']['GeoObjectCollection']['featureMember']
            if len(geo_objects) == 0:
                return None
            return geo_objects[0]['GeoObject']['Point']['pos']
    #
    # with open('res.json') as f:
    #     res_json = json.loads(f.read())
    #     res_dict = dict(res_json)
    #     geo_objects = res_dict['response']['GeoObjectCollection']['featureMember']
    #     if len(geo_objects) == 0:
    #         return None
    #     return geo_objects[0]['GeoObject']['Point']['pos']
