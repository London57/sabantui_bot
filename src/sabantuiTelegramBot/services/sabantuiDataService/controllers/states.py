from aiogram.fsm.state import State, StatesGroup

class SabantuiDataStates(StatesGroup):
    choose_category = State()
    competitions = State()