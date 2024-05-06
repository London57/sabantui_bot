from aiogram import Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from quizLogic.linked_list import QuestionNodeList



dp = Dispatcher()

quetionNodeList = QuestionNodeList()

@dp.message(CommandStart)
async def start(message: Message):
    keyboard = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton()
        ]
    ])