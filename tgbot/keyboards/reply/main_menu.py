from aiogram import types


def main_menu() -> types.ReplyKeyboardMarkup:
    keyboard = types.ReplyKeyboardMarkup(row_width=2)
    keyboard.add(
        types.KeyboardButton(text="👤 Mening kabinetim"),
    )
    return keyboard

