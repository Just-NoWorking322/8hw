from aiogram import types, Dispatcher
from kebooards import product_keyboard
from aiogram import types, Dispatcher
from kebooards import confirm_keyboard
from products import PRODUCTS

async def start_command(message: types.Message):
    await message.answer("Привет! Выберите товар:", reply_markup=product_keyboard())

def start_handler(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=["start"])

from aiogram import types, Dispatcher

async def help_command(message: types.Message):
    await message.answer("/start - начать заново\n/help - помощь\n/cankel - отменить заказ")

def help_handler(dp: Dispatcher):
    dp.register_message_handler(help_command, commands=["help"])
    


async def cancel_command(message: types.Message):
    await message.answer("Заказ отменён. Выберите товар:", reply_markup=product_keyboard())

def cancel_handler(dp: Dispatcher):
    dp.register_message_handler(cancel_command, commands=["cancel"])


async def product_callback(call: types.CallbackQuery):
    product_id = int(call.data.split("_")[1])
    product = PRODUCTS[product_id]
    await call.message.answer(
        f"Вы выбрали:\nНазвание: {product['name']}\nОписание: {product['description']}\nЦена: {product['price']}",
        reply_markup=confirm_keyboard(),
    )

async def order_callback(call: types.CallbackQuery):
    await call.message.answer("Ваш заказ принят! (Отправка данных на почту имитируется в консоли)")
    print("Заказ: Подробности заказа отображаются в консоли.")  

def order_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(product_callback, lambda c: c.data.startswith("product_"))
    dp.register_callback_query_handler(order_callback, text="confirm_order")
