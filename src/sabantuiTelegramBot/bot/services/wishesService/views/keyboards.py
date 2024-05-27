from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_cancel_kbd():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='Отмена'),
            ],
        ],
        resize_keyboard=True
    )