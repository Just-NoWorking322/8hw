import smtplib
from email.mime.text import MIMEText
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from config import token, smtp_server, smtp_port, smtp_user, smtp_password
import re
import logging
from aiosqlite import connect as async_connect
from aiogram import Router

bot = Bot(token=token) 
dp = Dispatcher()
dp.include_router(Router())

logging.basicConfig(level=logging.INFO)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
