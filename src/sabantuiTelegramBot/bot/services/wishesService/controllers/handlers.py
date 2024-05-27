from aiogram import Router, F
from aiogram.filters import Command, and_f
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
from ..models.db.repositoryServices import WishesRepositoryService
from ..models.db.init_db import create_wishes_db_model
from ..views.keyboards import get_cancel_kbd
from .states import WishesState
from datetime import datetime


wishes = Router()

repo = WishesRepositoryService(create_wishes_db_model())


@wishes.message(and_f(Command('wish'), StateFilter(None)))
async def start_wish(message: Message, state: FSMContext):
    await message.answer(
        'Поделитесь впечатлениями о празднике, скажите, что Вам понравилось, а что нет, может быть, у Вас есть какие-то пожелания, идеи? Поделитесь мнением. (Вы можете отправить несколько сообщений)',
        reply_markup=get_cancel_kbd()
        )
    await state.set_state(WishesState.wish)
    

@wishes.message(and_f(StateFilter(WishesState.wish), F.text))
async def wish_base(message: Message, state: FSMContext):
    if message.text != 'Отмена':
        repo.insert(message.from_user.id, message.from_user.username, message.text, datetime.now())
        await message.answer('Успешно сохранено')
    await state.clear()