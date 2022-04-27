from aiogram.types import InlineKeyboardMarkup
from aiogram.types.inline_keyboard import InlineKeyboardButton

add_dars_inline = InlineKeyboardMarkup()
add_dars_inline.add(InlineKeyboardButton(text="➕Dars qo'shish➕", callback_data="add_dars"))