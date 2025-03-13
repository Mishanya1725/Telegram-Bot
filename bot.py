import asyncio

from aiogram import Bot, Dispatcher
#.\venv\Scripts\activate ; python bot.py ; ctr + c
from config import API_BOT
from handlers.commands import router
from handlers.callback import call_router

async def main():
    try:
        bot = Bot(API_BOT)
        dp = Dispatcher()
        print('Bot Start')
        dp.include_router(router) # добавляем роутеры
        dp.include_router(call_router) # добавляем роутеры
        await dp.start_polling(bot)
    except Exception as ex:
        print(f'There is Exception{ex}')

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt: # Отвечает за выключение бота сочетанием клавиш ctrl + c
        print('Exit')