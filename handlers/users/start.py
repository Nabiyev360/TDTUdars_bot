from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import ADMINS
from loader import dp, db, bot, Bot
from keyboards.default.mainKeyboard import main_keyboard
from keyboards.inline.channelsKeyboard import channel_keyboard

channels = {
    'Yoshlar news':[-1001082347664, 'tstu_yoshlari'], # Yoshlar news
    'TDTrU_online':[-1001414064363, 'tstu_online']  # TDTrU_online
    }

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
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
    else:
        await message.answer(f"Salom {message.from_user.full_name}😊. \nDars jadvalini ko'rish uchun hafta kunini tanlang!💁‍♂️", reply_markup = main_keyboard)

        db.add_user(message.chat.id, message.from_user.full_name, message.from_user.username)