from datetime import datetime
from aiogram import Dispatcher, F
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart, Command, StateFilter, and_f
from aiogram.types import Message
from aiogram.types import ReplyKeyboardRemove
from .state import States
from ..models.quizService.quetionList import QuestionList
from ..models.db.repositories import QuizRepositoryService
from ..models.db.init_db import create_db_model
from ..views.keyboards import get_accept_to_quiz_kbd, get_quiz_kbd
from ..views.quiz_start import quiz_start_message


dp = Dispatcher()
repo = QuizRepositoryService(create_db_model())
questionList = QuestionList()


@dp.message(CommandStart())
async def start(message: Message):
    return message.answer('start')

@dp.message(and_f(Command('quiz')), StateFilter(None))
async def start_quiz(message: Message, state: FSMContext):
    await state.set_state(States.PreQuiz)
    await message.answer(
        quiz_start_message,
        reply_markup=get_accept_to_quiz_kbd()
        )


@dp.message(and_f(StateFilter(States.PreQuiz)), F.text)
async def pre_quiz(message: Message, state: FSMContext):
    if message.text not in ("да", "отмена"):
        await start_quiz(message, state)
    elif message.text == 'отмена':
        await quit_quiz(message, state)
    else:
        await state.set_state(States.Quiz)
        await state.set_data({'time_start': datetime.now()})
        await quiz(message, state)


async def quit_quiz(message: Message, state: FSMContext):
    await message.answer(
        'Вы покинули квиз.',
        reply_markup=ReplyKeyboardRemove(),
        )


@dp.message(and_f(StateFilter(States.Quiz)), F.text == 'Вернуться к предыдущему вопросу')
async def return_to_before_question(message: Message, state: FSMContext):
    question, indexQuestion = questionList.back()
    await message.answer(
        f"{indexQuestion}. {question.question}",
        reply_markup=get_quiz_kbd(question, questionList.tail.index),
    )


@dp.message(and_f(StateFilter(States.Quiz), F.text))
async def quiz(message: Message, state: FSMContext):
    # проверка выбора ответа из предложенных
    # если ответ не из преложенных, возвращаемся, а затем идём вперёд
    if questionList.tail and message.text not in questionList.tail.answers:
        await message.answer('Вы должны выбрать вариант ответа из предложенных!')
        if questionList.tail.index == 0:
            questionList.tail = None
            questionList.head = None
        else:
            questionList.back()

    try:
        question, questionBefore, indexQuestion = questionList.next()
    # если следующего вопроса нет
    except TypeError:
        question = False
        questionList.check_last_answer(message)

    if question:
        if questionList.tail.index > 0:
            questionList.check_right_answer(message, questionBefore)
        await message.answer(
            f"{indexQuestion}. {question.question}",
            reply_markup=get_quiz_kbd(question, questionList.tail.index),
        )
    else:
        await end_quiz(message, state)


async def end_quiz(message: Message, state: FSMContext):
    stateData = await state.get_data()
    right_answers_c, bad_answers_c, time = questionList.get_data_for_bd(stateData.get('time_start'))
    print(time)
    repo.insert(message.from_user.id, right_answers_c, bad_answers_c, time)
    await message.answer(f'Вы успешно прошли квиз! Правильных ответов: {right_answers_c}',
                         reply_markup=ReplyKeyboardRemove())
    await state.clear()
