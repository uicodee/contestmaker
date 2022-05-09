from aiogram import types

from tgbot.data.strings import subscribe_alert
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
        await query.answer(text=subscribe_alert, show_alert=True)
    else:
        if await user.get_user(user_id=query.from_user.id) is None:
            await user.add_user(
                user_id=query.from_user.id,
                name=query.from_user.full_name,
                username=query.from_user.username,
                subscribed=True,
                referrals=0
            )
        else:
            await user.update_status(user_id=query.from_user.id, subscribed=True)
        await query.message.delete()
