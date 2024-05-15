from aiogram import Dispatcher, F
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart, Command, StateFilter, and_f
from aiogram.types import Message
from aiogram.types import ReplyKeyboardRemove
from .quizLogic.quetionList import QuestionList
from .state import States
from .keyboards import get_quiz_kbd, get_accept_to_quiz_kbd


dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    return message.answer('start')

@dp.message(and_f(Command('quiz')), StateFilter(None))
async def start_quiz(message: Message, state: FSMContext):
    await state.set_state(States.PreQuiz)
    await message.answer('''Квиз можно будет проходит неограниченое число раз.\
                         Но в таблице лидеров будет результат первого прохождения.\
                         Вы уверены, что готовы? Если нет, то нажмите кнопку "отмена"''',
                         reply_markup=get_accept_to_quiz_kbd())


@dp.message(and_f(StateFilter(States.PreQuiz)), F.text)
async def pre_quiz(message: Message, state: FSMContext):
    global questionList
    questionList = QuestionList()
    if message.text not in ("да", "отмена"):
        await start_quiz(message, state)
    elif message.text == 'отмена':
        await quit_quiz(message, state)
    else:
        await state.set_state(States.Quiz)
        await quiz(message, state)


@dp.message(and_f(StateFilter(States.Quiz)), F.text == 'Вернуться к предыдущему вопросу')
async def return_to_before_question(message: Message, state: FSMContext):
    question, indexQuestion = questionList.back()
    await message.answer(
        f"{indexQuestion}. {question.question}",
        reply_markup=get_quiz_kbd(question, questionList.tail.index),
    )


@dp.message(and_f(StateFilter(States.Quiz)), F.text == 'Выйти из квиза')
async def quit_quiz(message: Message, state: FSMContext):
    await message.answer('Вы покинули квиз', reply_markup=ReplyKeyboardRemove())
    await state.clear()


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
    right_answers = questionList.count_right_answers()
    await message.answer(f'Вы успешно прошли квиз! Правильных ответов: {right_answers}',
                         reply_markup=ReplyKeyboardRemove())
    await state.clear()
