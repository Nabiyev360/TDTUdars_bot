from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

admin_cancel = InlineKeyboardMarkup()
admin_cancel.add(
    InlineKeyboardButton(text="✖️Cancel", callback_data='cancel_admin')
)