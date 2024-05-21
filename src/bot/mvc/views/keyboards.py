from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from random import shuffle
from ..models.quizService.types import Question


def get_accept_to_quiz_kbd():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="да"),
            ],
            [
                KeyboardButton(text="отмена"),
            ],
        ], resize_keyboard=True
    )

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
    ], resize_keyboard=True)
    if QuestionList_tail_index > 0:
        kbd_markup.keyboard.append([
                KeyboardButton(text='Вернуться к предыдущему вопросу'),
            ])
    return kbd_markup
