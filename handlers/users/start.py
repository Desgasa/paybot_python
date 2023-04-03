from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp
from app import db
import logging
from buttons import profile_buttons

logging.basicConfig(level=logging.INFO)

 
@dp.message_handler(CommandStart())
async def start(call: types.Message):
        if(not db.subscriber_exists(call.from_user.id)):
            db.add_user(call.from_user.id)
            await call.answer("Добро пожаловать!\n Укажите как я могу к вам обращаться")
        else:
                result = db.username_exists(call.from_user.id)
                username = result[0]
                if username == None:
                        await call.answer("Введите, пожалуйста, как я могу к вам обращаться")
                else:
                      await call.answer("Добро пожаловать " + str(username), reply_markup=profile_buttons.startButton)      

