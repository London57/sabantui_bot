from aiogram.fsm.state import State, StatesGroup


class States(StatesGroup):
    PreQuiz = State()
    Quiz = State()
