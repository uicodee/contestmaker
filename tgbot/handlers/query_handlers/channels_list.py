from aiogram import types

from tgbot.data.strings import saved_channels, empty_channels, main_menu_btn
from tgbot.keyboards.inline.channels_list import channels_list_keyboard
from tgbot.service.repo.channel_repo import ChannelRepo
from tgbot.service.repo.repository import SQLAlchemyRepos


async def channels_list(query: types.CallbackQuery, repo: SQLAlchemyRepos):
    channel = repo.get_repo(ChannelRepo)
    channels = await channel.get_channels()
    print(channels)
    if not channels:
        await query.message.edit_text(
            text=empty_channels,
            reply_markup=types.InlineKeyboardMarkup(
                row_width=1,
                inline_keyboard=[
                    [types.InlineKeyboardButton(text=main_menu_btn, callback_data='main_menu')]
                ]
            )
        )
    else:
        await query.message.edit_text(
            text=saved_channels,
            reply_markup=channels_list_keyboard(channels=channels)
        )
