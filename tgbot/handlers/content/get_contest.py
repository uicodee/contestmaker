from aiogram import types
from aiogram.dispatcher import FSMContext

from tgbot.service.repo.contest_repo import ContestRepo
from tgbot.service.repo.repository import SQLAlchemyRepos


async def get_contest_name(message: types.Message, state: FSMContext, repo: SQLAlchemyRepos):
    name = message.text
    contest = repo.get_repo(ContestRepo)
    data = await contest.add_contest(name=name)
    b = await message.bot.get_me()
    await message.answer(
        text=f'Konkurs nomi: {name}\n'
             f'Havola:\n'
             f'https://t.me/{b.username}?start=contest_{data}'
    )
