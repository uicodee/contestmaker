from aiogram import types
from aiogram.dispatcher import FSMContext

from tgbot.service.repo.channel_repo import ChannelRepo
from tgbot.service.repo.repository import SQLAlchemyRepos


async def add(query: types.CallbackQuery, state: FSMContext, repo: SQLAlchemyRepos):
    data = await state.get_data()
    channel = repo.get_repo(ChannelRepo)
    print(data.get('link'))
    await channel.add_channel(
        name=data.get('name'),
        link=data.get('link')
    )
    await query.answer(text=f'{data.get("link")} kanali ma\'lumotlar omboriga qo\'shildi', show_alert=True)
    await query.message.delete()
