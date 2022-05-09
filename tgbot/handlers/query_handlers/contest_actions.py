from aiogram import types

from tgbot.data.strings import empty_contest, main_menu_btn, saved_contests, contest_info, back
from tgbot.keyboards.inline.contests_keyboard import contests_list_keyboard
from tgbot.service.repo.contest_repo import ContestRepo
from tgbot.service.repo.repository import SQLAlchemyRepos


async def delete_contest(query: types.CallbackQuery, repo: SQLAlchemyRepos, callback_data: dict):
    contest = repo.get_repo(ContestRepo)
    await contest.delete_cont(contest_id=int(callback_data.get('contest_id')))
    contests = await contest.get_contest()
    if not contests:
        await query.message.edit_text(
            text=empty_contest,
            reply_markup=types.InlineKeyboardMarkup(
                row_width=1,
                inline_keyboard=[
                    [types.InlineKeyboardButton(text=main_menu_btn, callback_data='main_menu')],
                ]
            )
        )
    else:
        await query.message.edit_text(
            text=saved_contests,
            reply_markup=contests_list_keyboard(contests=contests)
        )


async def view_contest(query: types.CallbackQuery, repo: SQLAlchemyRepos, callback_data: dict):
    contest_id = int(callback_data.get('contest_id'))
    contest = repo.get_repo(ContestRepo)
    contest_user = await contest.get_contest_id(contest_id=contest_id)
    bot_username = (await query.message.bot.get_me()).username
    await query.message.edit_text(
        text=contest_info.format(
            contest_id=contest_user.id,
            contest_name=contest_user.name,
            date=contest_user.created_at.strftime('%d.%m.%Y %H:%M'),
            bot_username=bot_username
        ),
        reply_markup=types.InlineKeyboardMarkup(
            row_width=1,
            inline_keyboard=[
                [types.InlineKeyboardButton(text=back, callback_data='back_contest')],
                [types.InlineKeyboardButton(text=main_menu_btn, callback_data='main_menu')],
            ]
        )
    )


async def back_contest(query: types.CallbackQuery, repo: SQLAlchemyRepos):
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


