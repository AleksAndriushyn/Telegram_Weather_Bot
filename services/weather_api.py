from functools import partial
import aiohttp
import typing
from config import WEATHER_API_KEY

API_URL: str = 'http://api.openweathermap.org/data/2.5/'

api_session = aiohttp.ClientSession()


async def get_url(*_, session: aiohttp.ClientSession = api_session, api_url: str = API_URL,
                  key: str = WEATHER_API_KEY, collection: str, city: str) -> tuple[int, typing.Any]:
    url = f'{api_url}{collection}?q={city}&appid={key}'
    async with session.get(url) as response:
        return response.status, await response.json()


get_weather = partial(get_url, collection='weather')
get_forecast = partial(get_url, collection='forecast')
