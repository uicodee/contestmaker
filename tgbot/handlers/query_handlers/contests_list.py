from aiogram import types

from tgbot.data.strings import empty_contest, main_menu_btn, saved_contests
from tgbot.keyboards.inline.contests_keyboard import contests_list_keyboard
from tgbot.service.repo.contest_repo import ContestRepo
from tgbot.service.repo.repository import SQLAlchemyRepos


async def contests_list(query: types.CallbackQuery, repo: SQLAlchemyRepos):
    contest = repo.get_repo(ContestRepo)
    contests = await contest.get_contest()
    if not contests:
        await query.message.edit_text(
            text=empty_contest,
            reply_markup=types.InlineKeyboardMarkup(
                row_width=1,
                inline_keyboard=[
                    [types.InlineKeyboardButton(text=main_menu_btn, callback_data='main_menu')]
                ]
            )
        )
    else:
        await query.message.edit_text(
            text=saved_contests,
            reply_markup=contests_list_keyboard(contests=contests)
        )
