from aiogram import types

from tgbot.data.strings import user_info
from tgbot.service.repo.repository import SQLAlchemyRepos
from tgbot.service.repo.user_repo import UserRepo


async def my_cabinet(message: types.Message, repo: SQLAlchemyRepos):
    user = repo.get_repo(UserRepo)
    u = await user.get_user(user_id=message.from_user.id)
    await message.answer(
        text=user_info.format(
            date=u.created_at.strftime('%d.%m.%Y %H:%M'),
            referral_count=u.referrals,
            username=(await message.bot.get_me()).username,
            user_id=message.from_user.id
        )
    )
