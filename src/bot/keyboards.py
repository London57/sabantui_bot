from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from random import shuffle
from .quizLogic.types import Question


def get_quiz_kbd(question: Question, QuestionList_tail_index):
    quiz_list = [question.bad_answers[0], question.bad_answers[1], question.good_answer]
    shuffle(quiz_list)

    kbd_markup = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text=quiz_list[0]),
        ],
        [
            KeyboardButton(text=quiz_list[1]),
        ],
        [
            KeyboardButton(text=quiz_list[2]),
        ],
        [
            KeyboardButton(text='Выйти из квиза'),
        ],
    ], resize_keyboard=True)
    if QuestionList_tail_index > 0:
        kbd_markup.keyboard[3] = [
                KeyboardButton(text='Вернуться к предыдущему вопросу'),
            ]
        kbd_markup.keyboard.append(
            [
                KeyboardButton(text='Выйти из квиза'),
            ]
        )
    return kbd_markup
