from aiogram.types import Message
from aiogram import Router

r1 = Router()


@r1.message(commands="test1")
async def cmd_test1(message: Message):
    await message.answer("This is test 1")
