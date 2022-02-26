import asyncio

from aiogram import Bot, Dispatcher
from magic_filter import F
from bot.handlers.for_admins import admin_router
from bot.handlers.for_everyone import user_router


TOKEN = ""
bot = Bot(TOKEN, parse_mode="HTML")

ADMIN_ID = 1234567  # Place your Telegram ID here
admin_router.message.filter(F.chat.id == ADMIN_ID)

dp = Dispatcher()
dp.include_router(admin_router)
dp.include_router(user_router)


async def main() -> None:
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
