from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

profile = KeyboardButton("👤 ПРОФИЛЬ")
subscrip = KeyboardButton("🤍 ПОДПИСКА")

startButton = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
startButton.add(profile,subscrip)