from aiogram import types

from tgbot.callback_datas.callback_datas import cb_channel_delete, cb_channel_view
from tgbot.models import Channel


def channels_list_keyboard(channels: list[Channel]) -> types.InlineKeyboardMarkup:
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    for channel in channels:
        keyboard.add(
            types.InlineKeyboardButton(text=f"{channel.name}", callback_data=cb_channel_view.new(channel_id=channel.id)),
            types.InlineKeyboardButton(text="🗑", callback_data=cb_channel_delete.new(channel_id=channel.id)),
        )

    return keyboard
