from aiogram import types

from tgbot.keyboards.inline.contests_keyboard import contests_list_keyboard
from tgbot.service.repo.contest_repo import ContestRepo
from tgbot.service.repo.repository import SQLAlchemyRepos


async def contests_list(query: types.CallbackQuery, repo: SQLAlchemyRepos):
    contest = repo.get_repo(ContestRepo)
    contests = await contest.get_contest()
    await query.message.edit_text(
        text='Sizda saqlangan konkurslar ro\'yxati\n',
        reply_markup=contests_list_keyboard(contests=contests)
    )
