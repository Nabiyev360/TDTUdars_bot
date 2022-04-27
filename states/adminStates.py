from aiogram.dispatcher.filters.state import State, StatesGroup

class AdminState(StatesGroup):
    waiting_admin_message = State()
    waiting_admin_channel = State()