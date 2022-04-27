from aiogram.types import InlineKeyboardMarkup
from aiogram.types.inline_keyboard import InlineKeyboardButton


days_list= ["Dushanba", "Payshanba", "Seshanba", "Juma", "Chorshanba", "Shanba"]

days_inline = InlineKeyboardMarkup(row_width=2)
for i in days_list:
    days_inline.insert(InlineKeyboardButton(text = '📝'+i, callback_data='edit'+i))
days_inline.add(InlineKeyboardButton(text = '🔙Orqaga', callback_data= 'main'))