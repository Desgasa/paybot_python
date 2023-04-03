from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from loader import dp

import logging

logging.basicConfig(level=logging.INFO)

@dp.message_handler(CommandHelp())
async def help(call: types.Message):       
            text = ("Список команд: ",
            "/start - Начать диалог",
            "/help - Помощь"
            "/randompassword - Рандомный пароль",
            "/russianroulette - Русская рулетка")

            await call.answer("\n".join(text))