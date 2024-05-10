from aiogram import Dispatcher, F
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart, Command, StateFilter, and_f
from aiogram.types import Message
from aiogram.types import ReplyKeyboardRemove
from .quizLogic.quetionList import QuestionList
from .state import States
from .keyboards import get_quiz_kbd
from .quizLogic.checkRightAnswer import check_right_answer

dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    return message.answer('start')

@dp.message(Command('quiz'))
async def start_quiz(message: Message, state: FSMContext):
    global questionList
    questionList = QuestionList()
    await state.set_state(States.Quiz)
    await quiz(message, state)

@dp.message(and_f(StateFilter(States.Quiz), F.text))
async def quiz(message: Message, state: FSMContext):
    question, questionBefore = questionList.next()
    if questionList.tail.index > 0:
        print(check_right_answer(message, questionBefore, questionList))
    if question:
        await message.answer(
            question['question'],
            reply_markup=get_quiz_kbd(question),
        )
    else:
        await end_quiz(message, state)


async def end_quiz(message: Message, state: FSMContext):
    await message.answer('Вы успешно прошли квиз!', reply_markup=ReplyKeyboardRemove())
    await state.clear()

async def end_quiz(message: Message, state: FSMContext):
    await message.answer('Вы успешно прошли квиз!', reply_markup=ReplyKeyboardRemove())
    await state.clear()
