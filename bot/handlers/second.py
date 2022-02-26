from aiogram.types import Message
from aiogram import Router

r2 = Router()


@r2.message(commands="test2")
async def cmd_test2(message: Message):
    await message.answer("This is test 2")
