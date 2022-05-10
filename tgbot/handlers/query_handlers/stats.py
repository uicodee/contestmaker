from datetime import datetime

from aiogram import types

from tgbot.data.strings import stats_info, main_menu_btn
from tgbot.service.repo.contest_repo import ContestRepo
from tgbot.service.repo.repository import SQLAlchemyRepos
from tgbot.service.repo.user_repo import UserRepo


async def stats(query: types.CallbackQuery, repo: SQLAlchemyRepos):
    await query.message.edit_text(
        text=stats_info.format(
            users_count=await repo.get_repo(UserRepo).count_user(),
            contest_count=len(await repo.get_repo(ContestRepo).get_contest()),
            finished_contest=len(await repo.get_repo(ContestRepo).get_contest_finished()),
            today_users=await repo.get_repo(UserRepo).today_users(date=datetime.strptime(datetime.now().strftime('%Y-%m-%d'), '%Y-%m-%d'))
        ),
        reply_markup=types.InlineKeyboardMarkup(
            row_width=1,
            inline_keyboard=[
                [types.InlineKeyboardButton(text=main_menu_btn, callback_data='main_menu')]
            ]
        )
    )
