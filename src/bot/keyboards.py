from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from random import shuffle


def get_quiz_kbd(quiz_dict: dict):
    quiz_list = [quiz_dict['bad_answers'][0], quiz_dict['bad_answers'][1], quiz_dict['good_answer']]
    shuffle(quiz_list)
    
    return ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text=quiz_list[0]),
        ],
        [
            KeyboardButton(text=quiz_list[1]),
        ],
        [
            KeyboardButton(text=quiz_list[2])
        ]
    ], resize_keyboard=True)
