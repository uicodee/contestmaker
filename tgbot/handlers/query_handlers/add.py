from aiogram import types
from aiogram.dispatcher import FSMContext

from tgbot.data.strings import addedd_channel
from tgbot.service.repo.channel_repo import ChannelRepo
from tgbot.service.repo.repository import SQLAlchemyRepos


async def add(query: types.CallbackQuery, state: FSMContext, repo: SQLAlchemyRepos):
    data = await state.get_data()
    channel = repo.get_repo(ChannelRepo)
    await channel.add_channel(
        name=data.get('name'),
        link=data.get('link')
    )
    await query.answer(text=addedd_channel.format(link=data.get('link')), show_alert=True)
    await query.message.delete()
