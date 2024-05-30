from aiogram import F
from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command, StateFilter, and_f
from aiogram.types import Message, ReplyKeyboardRemove
from ..views.keyboards import get_start_kbd, get_competitions_kbd
from ..views.messages import send_info, send_competitions
from ..models.categories import Categories, Competitions
from .states import SabantuiDataStates


sabantui_data = Router()

# для получения id фото
# @sabantui_data.message(and_f(StateFilter(None), F.photo))
# async def photo(message: Message):
#     await message.answer(str(message.photo[-1]))


@sabantui_data.message(and_f(StateFilter(None), Command('info')))
async def start_data(message: Message, state: FSMContext):
    await message.answer(
        'Нажимайте на кнопки и просматривайте информацию о Сабантуе',
        reply_markup=get_start_kbd()
        )
    await state.set_state(SabantuiDataStates.choose_category)


@sabantui_data.message(and_f(StateFilter(SabantuiDataStates.choose_category), F.text))
async def choose_category(message: Message, state: FSMContext):
    if message.text == 'Выйти':
        await message.answer(
            'Вы вышли.',
            reply_markup=ReplyKeyboardRemove()
        )
        await state.clear()
        return

    elif message.text not in [category['name'] for category in Categories.categories] and message.text != 'Вернуться назад':
        await message.answer('Выберите только из предложенных категорий')
        await state.clear()
        await start_data(message, state)
        return

    elif message.text == 'Состязания':
        await message.answer(
            'Выберите состязание',
            reply_markup=get_competitions_kbd()
        )
        await state.set_state(SabantuiDataStates.competitions)
        return
    else:
        data = send_info(message.text)
        await message.answer(data[0], parse_mode='Markdown')
    await state.clear()
    await start_data(message, state)


@sabantui_data.message(and_f(StateFilter(SabantuiDataStates.competitions), F.text))
async def competitions(message: Message, state: FSMContext):
    if message.text == 'Вернуться назад':
        # await choose_category(message, state)
        await state.clear()
        await start_data(message, state)
        return
    elif message.text not in [competition['name'] for competition in Competitions.competitions]:
        await message.answer('Выберите только из предложенных состязаний!')
        return
    data = send_competitions(message.text)
    await message.answer(data[0], parse_mode='Markdown')
