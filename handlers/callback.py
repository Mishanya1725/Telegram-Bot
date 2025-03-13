from aiogram import F, Router
from aiogram.types import Message, CallbackQuery

call_router = Router()

import keyboard.inline_kb as ikb

@call_router.message(F.text == 'Меню')
async def menu(message: Message):
    await message.answer('Выберите пункт меню:', reply_markup=ikb.inline_kb)

@call_router.message(F.text == 'Поддержка')
async def menu(message: Message):
    await message.answer('По всем вопросам - @misha_nya911')

@call_router.message(F.text == 'Информация')
async def menu(message: Message):
    await message.answer('Тут могла бы быть иформация о боте')

@call_router.message(F.text == 'Назад')
async def menu(message: Message):
    await message.answer('Выберите пункт меню:')

@call_router.callback_query(F.data == 'drinks')
async def drinks(callback: CallbackQuery): #Мы принимаем Callback запрос
    await callback.answer('Вы выбрали напитки')
    await callback.message.answer('Напитки:', reply_markup=await ikb.drinks_list())

@call_router.callback_query(F.data == 'pizza')
async def drinks(callback: CallbackQuery): #Мы принимаем Callback запрос
    await callback.answer('Вы выбрали пиццы')
    await callback.message.answer('Пиццы:\nПеперонни\n4 Сыра\nГрибная')

@call_router.callback_query(F.data == 'salat')
async def drinks(callback: CallbackQuery): #Мы принимаем Callback запрос
    await callback.answer('Вы выбрали салаты')
    await callback.message.answer('Салаты:\nЦезарь\nОливье\nДомашний')