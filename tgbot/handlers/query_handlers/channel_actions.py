from aiogram import types

from tgbot.keyboards.inline.channels_list import channels_list_keyboard
from tgbot.service.repo.channel_repo import ChannelRepo
from tgbot.service.repo.repository import SQLAlchemyRepos


async def delete_channel(query: types.CallbackQuery, repo: SQLAlchemyRepos, callback_data: dict):
    channel = repo.get_repo(ChannelRepo)
    channel_name = await channel.get_channel(channel_id=int(callback_data.get('channel_id')))
    await channel.delete_channel(channel_id=int(callback_data.get('channel_id')))
    await query.answer(
        text=f"{channel_name.name} nomli {channel_name.link} kanali ma'lumotlar omboridan o'chirildi",
        show_alert=True
    )
    channels = await channel.get_channels()
    await query.message.edit_text(
        text='Sizda saqlangan kanallar ro\'yxati\n'
             'Kanal xavolasini ko\'rish uchun kanal nomini bosing',
        reply_markup=channels_list_keyboard(channels=channels)
    )


async def view_channel(query: types.CallbackQuery, repo: SQLAlchemyRepos, callback_data: dict):
    channel = repo.get_repo(ChannelRepo)
    channel_name = await channel.get_channel(channel_id=int(callback_data.get('channel_id')))
    await query.answer(
        text=channel_name.link,
        show_alert=True
    )
