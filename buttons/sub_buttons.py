from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


sub_markup = InlineKeyboardMarkup(row_width=1)
subMonth = InlineKeyboardButton(text="Оплатить 100 грн", callback_data='submonth')
sub_markup.insert(subMonth)