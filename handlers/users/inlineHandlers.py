from aiogram.types import CallbackQuery
from aiogram.dispatcher import FSMContext

from loader import dp
from states.newSience import NewSience
from keyboards.inline.buttonsInline import cancel
from keyboards.default.mainKeyboard import main_keyboard

@dp.callback_query_handler(text = 'add_dars')
async def add_dars(call: CallbackQuery, state = FSMContext):
    # Kun nomini olish:
    i = 0
    day = ''
    while call.message.text[i] != ' ':
        day+=call.message.text[i]
        i+=1
    await state.update_data(
       {f"day_name{call.message.chat.id}": day}
    )

    await call.message.delete()
    await call.message.answer(text=f"{day} kungi darslarni yuboring💁‍♂", reply_markup=cancel)

    # Yangi jadval qo'shish holat (state)iga tashlash
    await NewSience.sience_name.set()

@dp.callback_query_handler(text_contains = 'edit')
async def add_dars(call: CallbackQuery, state = FSMContext):
    day = call.data[4:]
    
    await state.update_data(
       {f"day_name{call.message.chat.id}": day}
    )
    
    await call.message.delete()
    await call.message.answer(text=f"{day} kungi darslarni kiriting", reply_markup=cancel)

    # Yangi jadval qo'shish holat (state)iga tashlash
    await NewSience.sience_name.set()
    
    
@dp.callback_query_handler(text = 'cancel', state=NewSience)
async def add_dars(call: CallbackQuery, state = FSMContext):
    await call.message.delete()
    await state.finish()                #state'dan chiqamiz ( & state datasi clear bo'ladi)
    await call.message.answer(text = "O'zgartirish bekor qilindi✅", reply_markup=main_keyboard)
    
    
@dp.callback_query_handler(text = 'main')
async def add_dars(call: CallbackQuery, state = FSMContext):
    await call.message.delete()
    await call.message.answer(text = "Main", reply_markup=main_keyboard)