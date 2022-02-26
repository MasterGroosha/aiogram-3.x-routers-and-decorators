from aiogram.types import Message
from aiogram import Router

user_router = Router()


@user_router.message(commands="user")
async def cmd_test2(message: Message):
    await message.answer("This is a router for users")
