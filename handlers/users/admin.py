import asyncio
from aiogram import types
from aiogram.dispatcher import FSMContext
from data.config import ADMINS
from loader import dp, db


from states.adminStates import AdminState
from keyboards.inline.adminCancel import admin_cancel

@dp.message_handler(text = "/count")
async def send_count_users(message: types.Message):
    await message.answer(db.count_users())


@dp.message_handler(user_id = ADMINS, text = "/message")
async def send_message_users(message: types.Message):
    await message.answer(text = "Foydalanuvchilarga yuborish kerak bo'lgan xabarni yuboring🔼\n\nBekor qilish uchun \"Cancel\"ni bosing",
        reply_markup = admin_cancel)
    
    await AdminState.waiting_admin_message.set()

@dp.message_handler(user_id = ADMINS, state = AdminState.waiting_admin_message, content_types= types.ContentType.ANY)
async def send_message_users(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('Xabar foydalanuvchilarga yuborilmoqda...')
    n = 0
    for i in db.get_users_id():
        user_id = i[0]
        try:
            await message.send_copy(chat_id = user_id)
            n+=1
        except:
            pass
        await asyncio.sleep(0.3)
    await message.answer(f'Xabar {n} ta foydalanuvchiga muvaffaqqiyatli yuborildi!')


@dp.callback_query_handler(user_id = ADMINS, state = '*', text = 'cancel_admin')
async def cancel_send_msg(call: types.CallbackQuery, state: FSMContext):
    await state.finish()
    await call.message.delete()
    await call.message.answer("Bekor qilindi!")



@dp.message_handler(chat_id= ADMINS)
async def send_message_users(message: types.Message):
    try:
        user_id = message.reply_to_message.forward_from.id
        await dp.bot.send_message(user_id, message.text)
        await message.answer("✅ Muvaffaqiyatli yuborildi")
    except Exception as ex:
        await message.reply(ex)
        await sleep(1)
        await message.reply('Foydalanuvchiga xabar yuborish uchun foydalanuvchidan kelgan xabarni tanlab oling💁‍♂️')

