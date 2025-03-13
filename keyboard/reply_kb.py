from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

reply_start = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Меню')],
    [KeyboardButton(text='Поддержка'),KeyboardButton(text='Информация')],
    [KeyboardButton(text='Назад')]
], resize_keyboard=True)

