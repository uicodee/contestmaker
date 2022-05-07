from aiogram import types

from tgbot.keyboards.inline.channels_list import channels_list_keyboard
from tgbot.service.repo.channel_repo import ChannelRepo
from tgbot.service.repo.repository import SQLAlchemyRepos


async def channels_list(query: types.CallbackQuery, repo: SQLAlchemyRepos):
    channel = repo.get_repo(ChannelRepo)
    channels = await channel.get_channels()
    await query.message.edit_text(
        text='Sizda saqlangan kanallar ro\'yxati\n'
             'Kanal xavolasini ko\'rish uchun kanal nomini bosing',
        reply_markup=channels_list_keyboard(channels=channels)
    )
