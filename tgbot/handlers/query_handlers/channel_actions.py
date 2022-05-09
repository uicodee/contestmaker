from aiogram import types

from tgbot.data.strings import deleted_channel, saved_channels, empty_channels, main_menu_btn
from tgbot.keyboards.inline.channels_list import channels_list_keyboard
from tgbot.service.repo.channel_repo import ChannelRepo
from tgbot.service.repo.repository import SQLAlchemyRepos


async def delete_channel(query: types.CallbackQuery, repo: SQLAlchemyRepos, callback_data: dict):
    channel = repo.get_repo(ChannelRepo)
    channel_name = await channel.get_channel(channel_id=int(callback_data.get('channel_id')))
    await channel.delete_channel(channel_id=int(callback_data.get('channel_id')))
    await query.answer(
        text=deleted_channel.format(channel_name=channel_name.name, channel_link=channel_name.link),
        show_alert=True
    )
    channels = await channel.get_channels()
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


async def view_channel(query: types.CallbackQuery, repo: SQLAlchemyRepos, callback_data: dict):
    channel = repo.get_repo(ChannelRepo)
    channel_name = await channel.get_channel(channel_id=int(callback_data.get('channel_id')))
    await query.answer(
        text=channel_name.link,
        show_alert=True
    )
