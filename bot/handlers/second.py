from aiogram.types import Message
from aiogram import Router

second_router = Router()


@second_router.message(commands="test2")
async def cmd_test2(message: Message):
    await message.answer("This is test 2")
