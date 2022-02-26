from aiogram import Bot, Dispatcher
from bot.handlers.first import r1
from bot.handlers.second import r2


TOKEN = ""
bot = Bot(TOKEN, parse_mode="HTML")
dp = Dispatcher()
dp.include_router(r1)
dp.include_router(r2)


def main() -> None:
    dp.run_polling(bot)


if __name__ == "__main__":
    main()