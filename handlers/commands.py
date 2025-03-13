from aiogram import Router, F
from aiogram.types import Message # Импортируем то, на какой тип данных будет отвечать бот - сообщения
from aiogram.filters import Command, CommandStart # filters - модуль команд

import keyboard.reply_kb as rkb

router = Router()

# роутеры - это компоненты которые позволяют группировать хэндлеры по определенным логическим кодам

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет! Я готов помогать', reply_markup=rkb.reply_start)

@router.message(Command('help'))
async def cmd_help(message: Message): # Принимает message типа Message
    await message.answer('По всем вопросам - @misha_nya911')

@router.message(F.text == "Привет")
async def cmd_hello(message: Message):
    name = message.from_user.first_name # бот обращается к нам по имени
    await message.answer(f'Привет  {name}!')


@router.message(F.photo) # Принимает сообщения типа photo 
async def cmd_phot(message: Message):
    photo = message.photo
    text = "Какое красивое фото!"
    await message.answer_photo(photo[0].file_id, text)

# @router.message()
# async def handle_messages(message: Message):
#     if message.text == 'Проверка':
#         await message.answer('Проверка успешна!')
#     else:
#         await message.answer('Я не знаю что ответить')









# @router.message(F.text) - echo bot
# async def cmd_hello(message: Message):
#     text = message.text
#     await message.answer(f"Вы написали: {text}")
