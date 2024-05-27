from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from ..models.messages import Categories
from ..models.categories import Competitions

def get_start_kbd():
    keyboard = [[KeyboardButton(text='Выйти')]]
    for category in Categories.categories:
        keyboard.append([KeyboardButton(text=category['name'])])

    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True
    )


def get_competitions_kbd():
    keyboard=[[KeyboardButton(text='Вернуться назад')]]
    for comp in Competitions.competitions:
        keyboard.append([KeyboardButton(text=comp['name'])])
   
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        
        resize_keyboard=True
    )