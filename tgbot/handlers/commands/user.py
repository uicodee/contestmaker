from aiogram import types

from tgbot.data.strings import main_menu_user, not_enough_referrals, link_erorr, already_added, \
    successfully_addedd
from tgbot.keyboards.reply.main_menu import main_menu
from tgbot.service.repo.contest_repo import ContestRepo
from tgbot.service.repo.contest_user_repo import ContestUserRepo
from tgbot.service.repo.referrals_repo import ReferralsRepo
from tgbot.service.repo.repository import SQLAlchemyRepos
from tgbot.service.repo.user_repo import UserRepo


async def referral_start(message: types.Message, repo: SQLAlchemyRepos):
    args = message.get_args()
    user = repo.get_repo(UserRepo)
    if await user.get_user(user_id=message.from_user.id) is None:
        await repo.get_repo(ReferralsRepo).add_referral(
            user_id=message.from_user.id,
            referrer_id=int(args),
            name=message.from_user.full_name,
            username=message.from_user.username
        )
        await user.add_user(
            user_id=message.from_user.id,
            name=message.from_user.full_name,
            username=message.from_user.username,
            subscribed=True,
            referrals=0
        )
        await user.increase_referrals(
            user_id=int(args),
            count=1
        )
        await message.answer(
            text=main_menu_user,
            reply_markup=main_menu()
        )
    else:
        await message.answer(
            text=main_menu_user,
            reply_markup=main_menu()
        )


async def contest_start(message: types.Message, repo: SQLAlchemyRepos):
    args = message.get_args()
    user = repo.get_repo(UserRepo)
    contest = repo.get_repo(ContestRepo)
    splitted = args.split('_')
    data = await user.get_user(user_id=message.from_user.id)
    print(data)
    if data is None:
        await user.add_user(
            user_id=message.from_user.id,
            name=message.from_user.full_name,
            username=message.from_user.username,
            subscribed=True,
            referrals=0
        )
        await message.answer(
            text=not_enough_referrals
        )
        await message.answer(
            text=main_menu_user,
            reply_markup=main_menu()
        )
    elif data.referrals < 5:
        await message.answer(
            text=not_enough_referrals
        )
    else:
        c = await contest.get_contest_id(contest_id=int(splitted[-1]))
        if c is None:
            await message.answer(
                text=link_erorr
            )
        else:
            if await repo.get_repo(ContestUserRepo).get_user_contest(user_id=message.from_user.id, contest_id=c.id) is None:
                await repo.get_repo(ContestUserRepo).add_contest_user(
                    user_id=message.from_user.id,
                    contest_id=int(splitted[-1])
                )
                await message.answer(
                    text=successfully_addedd
                )
            else:
                await message.answer(
                    text=already_added
                )


async def user_start(message: types.Message, repo: SQLAlchemyRepos):
    user = repo.get_repo(UserRepo)
    data = await user.get_user(user_id=message.from_user.id)
    if data is None:
        await user.add_user(
            user_id=message.from_user.id,
            name=message.from_user.full_name,
            username=message.from_user.username,
            subscribed=False,
            referrals=0
        )
        await message.answer(
            text=main_menu_user,
            reply_markup=main_menu()
        )
    else:
        await message.answer(
            text=main_menu_user,
            reply_markup=main_menu()
        )
