
from aiogram import types
from aiogram.types.message import ContentType
from loader import dp
from app import db
from loader import bot
import logging


from config import config
from buttons import profile_buttons
from buttons import back_button
from buttons import sub_buttons
from cheaktime import timemenedger
from handlers.users import randompass

import random
import time 




@dp.message_handler()
async def messageprofile(message: types.Message):
        if message.text == "👤 ПРОФИЛЬ":
                user_sub = timemenedger.time_sub_day(db.get_time_sub(message.from_user.id))
                if user_sub == False:
                        user_sub = "No"
                        db.updape_status(message.from_user.id, False)
                        db.updape_time_sub(message.from_user.id, 0)

                result_username = db.username_exists(message.from_user.id)
                result_status = db.status_exists(message.from_user.id)
                username = result_username[0]
                status = result_status[0]        
                

                if status == 0: 
                        text = (f"Добро пожаловать {username}",
                                "У вас не активная подиска на бот")
                        await message.answer("\n".join(text))
                elif status == 1: 
                        text = (f"Добро пожаловать {username}",
                                f"У вас активная подиска на бот ещё {user_sub}")
                        await message.answer("\n".join(text),reply_markup=back_button.backButton)
                elif username == None:
                        text = ("Вы не зарегестрировались на бота.",
                                "Для этого укажите ваш никнейм")
                        await message.answer("\n".join(text))
        elif message.text == "🤍 ПОДПИСКА":
                await message.answer("Описание",reply_markup= sub_buttons.sub_markup)

        elif message.text == "← НАЗАД":
                result = db.username_exists(message.from_user.id)
                username = result[0]
                await message.answer("Добро пожаловать " + str(username), reply_markup=profile_buttons.startButton)   

        for element in randompass.password_length:
                if message.text == str(element):
                        for elementlength in range(element):
                                randompass.passwords += random.choice(randompass.ally)
                        await message.answer("Вот ваш пароль " + str(randompass.passwords))        

        else:
                if db.get_singup(message.from_user.id) == 'setnickname': 
                        if (len(message.text) >= 15):
                                await message.answer("Ник должен быть больше 15 символов")
                        elif (len(message.text) <= 5):
                                await message.answer("Ник должен быть меньше 5 символов")
                        elif "@" in message.text:
                                await message.answer("В нике не должно быть символов")        
                        else:
                                await message.answer(f"Добро пожаловать {username}",reply_markup=profile_buttons.startButton)
                                db.updape_username(message.from_user.id, message.text)
                                db.updape_singup(message.from_user.id,'done')  
                               



@dp.callback_query_handler(text = "submonth")
async def submonth(call:types.CallbackQuery):
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await bot.send_invoice(chat_id=call.from_user.id, title="Оформление подписки", description="Описание товара", payload="month_sub",provider_token=config.LIQ_PayTOKEN, currency="UAH", start_parameter="test", prices=[{"label": "UAH", "amount": 10000}])

@dp.pre_checkout_query_handler()
async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
        await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def process_pay(message:types.Message):
        if message.successful_payment.invoice_payload == "month_sub":
                time_sub = int(time.time())+ timemenedger.days_to_seconds(30)
                db.updape_time_sub(message.from_user.id, time_sub)
                db.updape_status(message.from_user.id, True)
                await bot.send_message(message.from_user.id, "Вам выдана подписка на месяц")        
