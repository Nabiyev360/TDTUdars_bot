from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_keyboard = ReplyKeyboardMarkup(
    keyboard= [
        [
        KeyboardButton(text = "1️⃣ Dushanba"),
        KeyboardButton(text = "4️⃣ Payshanba")
        ],
        [
        KeyboardButton(text = "2️⃣ Seshanba"),
        KeyboardButton(text = "5️⃣ Juma")
        ],
        [
        KeyboardButton(text = "3️⃣ Chorshanba"),
        KeyboardButton(text = "6️⃣ Shanba")
        ],
        [
            KeyboardButton(text = "📝 Jadvalni o'zgartirish")    
        ],
        [
            KeyboardButton(text = "✍️ Izoh qoldirish")
        ]
    ],  
    one_time_keyboard=True, resize_keyboard=True)