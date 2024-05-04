from aiogram import Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message


dp = Dispatcher()

@dp.message(CommandStart)
async def start(message: Message):
    ...