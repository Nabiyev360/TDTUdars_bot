from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, db, Bot, bot
from keyboards.inline.addDarsInline import add_dars_inline
from keyboards.inline.editDarsInline import days_inline
from keyboards.inline.channelsKeyboard import channel_keyboard
from states.newSience import NewSience
from data.config import ADMINS

channels = {
    'Yoshlar news':[-1001082347664, 'tstu_yoshlari'], # Yoshlar news
    'TDTrU_online':[-1001414064363, 'tstu_online']  # TDTrU_online
    }

days_list = ["1️⃣ Dushanba", "2️⃣ Seshanba", "3️⃣ Chorshanba", "4️⃣ Payshanba", "5️⃣ Juma", "6️⃣ Shanba"]

@dp.message_handler(state=NewSience.sience_name)
async def new_siense(message: types.Message, state: FSMContext):
    data = await state.get_data()
    day_name = data.get(f"day_name{message.chat.id}").lower()
    chat_id= message.chat.id
    db.add_lessons(chat_id, day_name, message.text)
    
    await message.answer("Darslar ro'yxati muvaffaqiyatli qo'shildi✅", reply_markup = days_inline)
    await state.finish()
    await message.forward(ADMINS[0])

@dp.message_handler(text = '📝 Jadvalni o\'zgartirish')
async def edit_lesson(message: types.Message):
    await message.answer('Kiritmoqchi / O\'zgartirmochi bo\'lgan kuningizni tanlang', reply_markup=days_inline)

@dp.message_handler(text = '✍️ Izoh qoldirish')
async def send_lesson(message: types.Message):
    await message.answer('Bot haqida fikr, mulohaza va takliflaringiz bo\'lsa shu yergda yuboring💁‍♂')

@dp.message_handler()
async def send_dars(message: types.Message):
    # Majburiy azolik
    chek_list = []
    unfollow_channels = []
    info = Bot.get_current()
    for channel in channels:
        channel_id= channels[channel][0]
        channel_username= channels[channel][1]
        try:
            member = await info.get_chat_member(channel_id, message.from_user.id)
            if member.is_chat_member() == False:
                unfollow_channels.append([channel, channel_username])
                chek_list.append(False)   #True yoki False qo'shadi
        except:
            await bot.send_message(
                chat_id=ADMINS[0], text = f"Bot @{channel_username} kanaliga admin qilinmagan!")

    if False in chek_list:
        await message.answer(
            text = f"Assalomu alaykum😊. Botdan to'liq foydalanish uchun quyidagi kanallarga a'zo bo'ling va /start ni bosing",
            reply_markup=channel_keyboard(unfollow_channels))

    elif message.text in days_list:
        day_name= message.text[4:].lower()
        chat_id= message.chat.id
        lessons= db.get_lessons(chat_id=chat_id, day_name=day_name)
        
        keyboard = None
        if lessons== None:
            lessons= f'{day_name.title()} kunlik dars jadvali kiritilmagan'
            keyboard= add_dars_inline

        await message.answer(lessons, reply_markup=keyboard)
        await message.forward(ADMINS[0])

    elif message.text=='getdb':
        file = open('data/main.db', 'rb')
        await message.answer_document(file)
        file.close()

@dp.message_handler(content_types=['photo', 'audio', 'video', 'document', 'voice', 'gif', 'sticker'])
async def for_others(message: types.Message):
    await message.forward(ADMINS[0])