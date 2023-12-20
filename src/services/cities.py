import os
import aiohttp
import json
from dotenv import load_dotenv

load_dotenv()
GEOCODE_API_KEY = os.environ['GEOCODE_API_KEY']


async def parse_locality_name(text: str) -> str | None:
    words = text.split()
    if len(words) < 2:
        return None
    words.pop(0)
    return ' '.join(words)


async def get_settlements(name: str) -> list | None:
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
            settlements = find_settlements(name, geo_objects)
            if not settlements:
                return None
            return settlements


# Сложность: может быть несколько населённых пунктов с одинаковыми названиями
def find_settlements(city_name: str, geo_objects) -> list:
    city_name = city_name.lower()
    result = []
    for geo_object in geo_objects:
        settlements = [city_name, f'село {city_name}', f'посёлок {city_name}']
        if geo_object['GeoObject']['metaDataProperty']['GeocoderMetaData']['kind'] in ['locality', 'province'] and \
                geo_object['GeoObject']['name'].lower() in settlements:
            result.append(geo_object)
    return result


def parse_points(geo_object: dict) -> str:
    return geo_object['GeoObject']['Point']['pos']
