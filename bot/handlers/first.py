from aiogram.types import Message
from aiogram import Router

first_router = Router()


@first_router.message(commands="test1")
async def cmd_test1(message: Message):
    await message.answer("This is test 1")
