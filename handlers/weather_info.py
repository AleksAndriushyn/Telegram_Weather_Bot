import flag
from aiogram import types
from services import weather_api
from common import dp


@dp.message_handler()
async def weather_info(message: types.Message) -> None:
    status, body = await weather_api.get_weather(city=message.text)

    if status != 200:
        await message.answer(f'City {message.text} not found!')
        return
    text = (f'🌃: {body["name"]}{flag.flag(body["sys"]["country"])}\n'
            f'🌡: {int(body["main"]["temp"]) - 273}°C\n'
            f'Feels like: {int(body["main"]["feels_like"]) - 273}°C\n'
            f'💧: {body["main"]["humidity"]}%'
            )
    await message.answer(text)



