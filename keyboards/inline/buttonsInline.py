from aiogram.types import InlineKeyboardMarkup
from aiogram.types.inline_keyboard import InlineKeyboardButton

buttons = InlineKeyboardMarkup()
buttons.add(
    InlineKeyboardButton(text="✏", callback_data="edit_dars")
    )
    # InlineKeyboardButton(text="📤", switch_inline_query='Yaxshi')

cancel = InlineKeyboardMarkup()
cancel.add(
    InlineKeyboardButton(text="❎Bekor qilish", callback_data="cancel")
    )