from aiogram import types
from loader import dp
import logging



logging.basicConfig(level=logging.INFO)

password_length = [8,9,10,11,12,13,14,15,16]
digits = '0123456789'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase = 'abcdefghijklmnopqrstuvwxyz' 
punctuation = '!#$%&*+-=?@^_' 
ally = digits + uppercase + lowercase + punctuation
passwords = ''

@dp.message_handler(commands = ['randompassword'],commands_prefix = "/!")
async def randompass(message: types.Message):
    await message.answer("Введите сколько символов должно быть в пароле")
    

