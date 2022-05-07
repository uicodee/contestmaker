from aiogram import types

from tgbot.keyboards.inline.channels_list import channels_list_keyboard
from tgbot.service.repo.channel_repo import ChannelRepo
from tgbot.service.repo.repository import SQLAlchemyRepos
from tgbot.service.repo.user_repo import UserRepo


async def check_subscription(query: types.CallbackQuery, repo: SQLAlchemyRepos):
    channel = repo.get_repo(ChannelRepo)
    user = repo.get_repo(UserRepo)
    channels = await channel.get_channels()
    statuses = []
    for ch in channels:
        status = await query.message.bot.get_chat_member(
            chat_id=ch.link,
            user_id=query.from_user.id
        )
        statuses.append(status.status)
    if 'left' in statuses:
        await query.answer(text='Barcha kanallarga obuna bo\'ling!', show_alert=True)
    else:
        await user.update_status(user_id=query.from_user.id, subscribed=True)
        await query.message.delete()
