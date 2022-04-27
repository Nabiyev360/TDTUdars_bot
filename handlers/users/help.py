from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
        await message.answer('https://telegra.ph/Dars-Jadvali-bot-11-04')