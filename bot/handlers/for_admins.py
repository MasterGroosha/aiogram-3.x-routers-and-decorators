from aiogram.types import Message
from aiogram import Router

admin_router = Router()


@admin_router.message(commands="admin")
async def cmd_test1(message: Message):
    await message.answer("This is a handler for admins only")
