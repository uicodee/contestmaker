from aiogram import types

from tgbot.data.strings import cabinet_text


def main_menu() -> types.ReplyKeyboardMarkup:
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    keyboard.add(
        types.KeyboardButton(text=cabinet_text),
    )
    return keyboard

