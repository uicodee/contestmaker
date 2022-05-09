from aiogram import types
from aiogram.dispatcher import FSMContext

from tgbot.data.strings import check_data_contest, main_menu_btn
from tgbot.service.repo.contest_repo import ContestRepo
from tgbot.service.repo.repository import SQLAlchemyRepos


async def get_contest_name(message: types.Message, state: FSMContext, repo: SQLAlchemyRepos):
    name = message.text
    contest = repo.get_repo(ContestRepo)
    data = await contest.add_contest(name=name)
    b = await message.bot.get_me()
    await message.answer(
        text=check_data_contest.format(name=name, username=b.username, data=data),
        reply_markup=types.InlineKeyboardMarkup(
            row_width=1,
            inline_keyboard=[
                [types.InlineKeyboardButton(text=main_menu_btn, callback_data='main_menu')]
            ]
        )
    )
