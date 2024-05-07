from aiogram import Dispatcher, F
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart, Command, StateFilter, and_f
from aiogram.types import Message
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from .quizLogic.quetionList import QuestionList
from .state import States
from .keyboards import get_quiz_kbd


dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    return message.answer('start')

@dp.message(Command('quiz'))
async def start_quiz(message: Message, state: FSMContext):
    global questionList
    questionList = QuestionList()

    await state.set_state(States.Quiz)
    question = questionList.next()
    await message.answer(
        question['question'],
        reply_markup=get_quiz_kbd(question)
    )

@dp.message(and_f(StateFilter(States.Quiz), F.text))
async def quiz(message: Message, state: FSMContext):
    question = questionList.next()
    if question:
        await message.answer(
            question['question'],
            reply_markup=get_quiz_kbd(question),
        )
    else:
        await state.clear()
        await message.answer('Вы успешно прошли квиз!')
        return
    # ЕЩЁ НУЖНО УДАЛИТЬ ОБЪЕКТ questionList!!!