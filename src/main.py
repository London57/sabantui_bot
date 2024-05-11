from bot.bot import bot
import asyncio
from bot.handlers import dp
from bot.commands import Commands
from aiogram.types import BotCommandScopeAllPrivateChats

ALLOWED_UPDATES = ['message']


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands(commands=Commands, scope=BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)


if __name__ == '__main__':
    asyncio.run(main())
