from aiogram.fsm.state import State, StatesGroup

class WishesState(StatesGroup):
    wish = State()