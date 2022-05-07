from aiogram import types


def admin_panel() -> types.InlineKeyboardMarkup:
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        types.InlineKeyboardButton(text="➕ Kanal qo'shish", callback_data="add_channel"),
        types.InlineKeyboardButton(text="📃 Kanallar ro'yxati", callback_data="channels_list"),
        types.InlineKeyboardButton(text="🎉 Konkurs yaratish", callback_data="add_contest"),
        types.InlineKeyboardButton(text="🎁 Konkurslar ro'yxati", callback_data="contests_list"),
    )

    return keyboard
