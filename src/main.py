from bot import bot
import asyncio
from aiogram import Dispatcher
from bot.quizService.controllers.handlers import quiz
from bot.commands import Commands
from bot.quizService.models.db.init_db import init_db
from aiogram.types import BotCommandScopeAllPrivateChats

ALLOWED_UPDATES = ['message']


dp = Dispatcher()
dp.include_router(quiz)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=Commands, scope=BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)


if __name__ == '__main__':
    init_db()
    asyncio.run(main())











 