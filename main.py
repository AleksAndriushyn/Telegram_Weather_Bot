import asyncio
import logging
from common import dp, bot
from services import weather_api


async def main():
    import handlers
    logging.basicConfig(level=logging.INFO)
    try:
        await dp.start_polling()
    finally:
        await weather_api.api_session.close()
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.get_event_loop().run_until_complete(main())
    except (KeyboardInterrupt, SystemExit):
        logging.info("Bot stopped!")
