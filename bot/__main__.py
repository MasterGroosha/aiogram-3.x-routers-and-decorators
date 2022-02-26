import asyncio

from aiogram import Bot, Dispatcher
from bot.handlers.first import first_router
from bot.handlers.second import second_router


TOKEN = ""
bot = Bot(TOKEN, parse_mode="HTML")
dp = Dispatcher()
dp.include_router(first_router)
dp.include_router(second_router)


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
