import asyncio
from aiogram import Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import BotCommandScopeAllPrivateChats
from services.quizService.controllers.handlers import quiz_router
from services.wishesService.controllers.handlers import wishes
from services.sabantuiDataService.controllers.handleers import sabantui_data
from services.quizService.models.db.init_db import init_quiz_table
from services.wishesService.models.db.init_db import init_wishes_table
from bot import bot
from commands import Commands

ALLOWED_UPDATES = ['message']


dp = Dispatcher()

@dp.message(CommandStart())
async def start(message):
    return message.answer('По команде /quiz можете пройти квиз по Сабантую, но перед этим ознакомтесь с этим праздником по команде /info, если захотите посмотреть лидеров квиза, вам поможет команда /leaders. Так же можете написать свой отзыв о Сабантуе по команде /wish.')

dp.include_routers(quiz_router, wishes, sabantui_data)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=Commands, scope=BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES, commans=Commands)


if __name__ == '__main__':
    init_quiz_table()
    init_wishes_table()
    print('start')
    asyncio.run(main())











 