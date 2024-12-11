from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def product_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton("Товар 1", callback_data="product_0"),
        
        InlineKeyboardButton("Товар 2", callback_data="product_1"),
        
        InlineKeyboardButton("Товар 3", callback_data="product_2"),
        
    )
    return keyboard

def confirm_keyboard():
    keyboard = InlineKeyboardMarkup()
    keyboard.add(
        InlineKeyboardButton("Подтвердить заказ", callback_data="confirm_order"),
        
        InlineKeyboardButton("Отменить", callback_data="cancel_order"),
        
    )
    return keyboard
