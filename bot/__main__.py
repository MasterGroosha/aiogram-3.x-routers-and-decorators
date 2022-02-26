import asyncio

from aiogram import Bot, Dispatcher
from magic_filter import F
from bot.handlers.for_admins import admin_router
from bot.handlers.for_everyone import user_router


TOKEN = ""
ADMIN_ID = 1234567  # Place your Telegram ID here


async def main() -> None:
    # Initialize bot and dispatcher
    bot = Bot(TOKEN, parse_mode="HTML")
    dp = Dispatcher()

    # Add admin filter to admin_router
    admin_router.message.filter(F.chat.id == ADMIN_ID)

    # Add routers to dispatcher
    dp.include_router(admin_router)
    dp.include_router(user_router)

    # [optional] Skip pending updates
    # await bot.delete_webhook(drop_pending_updates=True)

    # Run polling
    await dp.start_polling(bot)


asyncio.run(main())
