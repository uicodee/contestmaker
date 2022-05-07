from aiogram import types

from tgbot.models.channel import Channel


def channels_keyboard(channels: list[Channel]) -> types.InlineKeyboardMarkup:
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    for channel in channels:
        keyboard.insert(
            types.InlineKeyboardButton(text=channel.name, url=f'https://t.me/{channel.link}')
        )
    keyboard.add(
        types.InlineKeyboardButton(text='Obuna bo\'ldim', callback_data='check_subscription')
    )

    return keyboard
