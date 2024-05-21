from bot.mvc.controllers.bot import bot
import asyncio
from bot.mvc.controllers.handlers import dp
from bot.mvc.views.commands import Commands
from bot.mvc.models.db.init_db import init_db
from aiogram.types import BotCommandScopeAllPrivateChats

ALLOWED_UPDATES = ['message']


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=Commands, scope=BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)


if __name__ == '__main__':
    init_db()
    asyncio.run(main())











 