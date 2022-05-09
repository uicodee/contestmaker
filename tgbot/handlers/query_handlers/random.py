from aiogram import types
from aiogram.dispatcher import FSMContext

from tgbot.callback_datas.callback_datas import cb_select_count
from tgbot.config import Config
from tgbot.data.strings import empty_contest, main_menu_btn, select_saved_contest, select_count, check_random_info, \
    cancel, start, winner_congrats
from tgbot.keyboards.inline.contests_keyboard import contests_list_select
from tgbot.service.repo.contest_repo import ContestRepo
from tgbot.service.repo.contest_user_repo import ContestUserRepo
from tgbot.service.repo.repository import SQLAlchemyRepos
from tgbot.service.repo.user_repo import UserRepo
from tgbot.states.states import RandomForm


async def random(query: types.CallbackQuery, repo: SQLAlchemyRepos):
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
            text=select_saved_contest,
            reply_markup=contests_list_select(contests=contests)
        )
        await RandomForm.contest_id.set()


async def select_contest(query: types.CallbackQuery, callback_data: dict, state: FSMContext):
    contest_id = int(callback_data.get('contest_id'))
    await state.update_data(contest_id=contest_id)
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    for i in range(1, 10):
        keyboard.insert(
            types.InlineKeyboardButton(text=str(i), callback_data=cb_select_count.new(count=str(i)))
        )
    await query.message.edit_text(
        text=select_count,
        reply_markup=keyboard
    )
    await RandomForm.winners.set()


async def select_count_winners(query: types.CallbackQuery, callback_data: dict, state: FSMContext, repo: SQLAlchemyRepos):
    count = int(callback_data.get('count'))
    await state.update_data(winners=count)
    data = await state.get_data()
    contest = repo.get_repo(ContestRepo)
    c = await contest.get_contest_id(
        contest_id=data.get('contest_id')
    )
    await state.update_data(count=count)
    await query.message.edit_text(
        text=check_random_info.format(
            contest_id=c.id,
            contest_name=c.name,
            registered=len(await repo.get_repo(ContestUserRepo).get_contest_users(contest_id=int(data.get('contest_id')))),
            winners_count=count,
        ),
        reply_markup=types.InlineKeyboardMarkup(
            row_width=1,
            inline_keyboard=[
                [types.InlineKeyboardButton(text=start, callback_data='start_random')],
                [types.InlineKeyboardButton(text=cancel, callback_data='cancel')],
            ]
        )
    )
    await state.reset_state(with_data=False)


async def start_randomise(query: types.CallbackQuery, state: FSMContext, repo: SQLAlchemyRepos):
    m = await query.message.edit_text(text='⏳')
    data = await state.get_data()
    contest_id = int(data.get('contest_id'))
    c = await repo.get_repo(ContestRepo).get_contest_id(contest_id=contest_id)
    winners = int(data.get('winners'))
    data = await repo.get_repo(ContestUserRepo).select_random_user(contest_id=contest_id, winners=winners)
    winners_list = []
    config: Config = query.message.bot.get('config')
    while config.tg_bot.admin_id in [x.user_id for x in data]:
        data = await repo.get_repo(ContestUserRepo).select_random_user(contest_id=contest_id, winners=winners)
    for index, item in enumerate(data):
        u = await repo.get_repo(UserRepo).get_user(user_id=item.user_id)
        winners_list.append(
            f"{index + 1}. <a href='{item.user_id}'>{u.name}</a>\n"
        )
        await query.message.bot.send_message(
            chat_id=item.user_id,
            text=winner_congrats.format(contest_name=c.name)
        )
    await m.edit_text(
        text="G'oliblarni tabriklaymiz!\n\n" + "".join(winners_list)
    )
    await repo.get_repo(ContestRepo).update_status(contest_id=contest_id, finished=True)
