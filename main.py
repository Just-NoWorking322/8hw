import asyncio
from aiogram import Bot, Dispatcher
from config import token
from handlers.start import register_start_handler
from handlers.help import register_help_handler
from handlers.cancel import register_cancel_handler
from handlers.order import register_order_handlers

async def main():
    bot = Bot(token=token)
    dp = Dispatcher()

    register_start_handler(dp)
    register_help_handler(dp)
    register_cancel_handler(dp)
    register_order_handlers(dp)
    
    print("Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

