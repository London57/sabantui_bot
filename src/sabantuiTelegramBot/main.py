import asyncio
from aiogram import Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import BotCommandScopeAllPrivateChats
from bot.services.quizService.controllers.handlers import quiz
from bot.services.wishesService.controllers.handlers import wishes
from bot.services.sabantuiDataService.controllers.handleers import sabantui_data
from bot.services.quizService.models.db.init_db import init_quiz_table
from bot.services.wishesService.models.db.init_db import init_wishes_table
from bot import bot
from bot.commands import Commands

# ALLOWED_UPDATES = ['message']


dp = Dispatcher()

@dp.message(CommandStart())
async def start(message):
    return message.answer('По команде /quiz можете пройти квиз по Сабантую, но перед этим ознакомтесь с этим праздником по команде /info, если захотите посмотреть лидеров квиза, вам поможет команда /leaders')

dp.include_routers(quiz, wishes, sabantui_data)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=Commands, scope=BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot)


if __name__ == '__main__':
    init_quiz_table()
    init_wishes_table()
    asyncio.run(main())











 