from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


randompass = KeyboardButton("🎲 ПАРОЛЬ")


randompassButton = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
randompassButton.add(randompass)