from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

back = KeyboardButton("← НАЗАД")

backButton = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
backButton.add(back)