from aiogram import Dispatcher
from aiogram.types import Message

from tgbot.keyboards.inline.channels_keyboard import channels_keyboard
from tgbot.keyboards.reply.main_menu import main_menu
from tgbot.service.repo.channel_repo import ChannelRepo
from tgbot.service.repo.contest_repo import ContestRepo
from tgbot.service.repo.repository import SQLAlchemyRepos
from tgbot.service.repo.user_repo import UserRepo


async def user_start(message: Message, repo: SQLAlchemyRepos):
    user = repo.get_repo(UserRepo)
    channels = await repo.get_repo(ChannelRepo).get_channels()
    data = await user.get_user(user_id=message.from_user.id)
    if data is None:
        await user.add_user(
            user_id=message.from_user.id,
            name=message.from_user.full_name,
            subscribed=False
        )
        await message.answer(
            text='Assalomu Alaykum, quyidagi kanallarga obuna bo\'ling',
            reply_markup=channels_keyboard(channels=channels)
        )
    elif data.subscribed is False:
        await message.answer(
            text='Assalomu Alaykum, quyidagi kanallarga obuna bo\'ling',
            reply_markup=channels_keyboard(channels=channels)
        )
    else:
        args = message.get_args()
        if not args:
            await message.answer(
                text='Asosiy menu',
                reply_markup=main_menu()
            )
        else:
            contest_id = args.split('_')
            if 'contest' in contest_id:
                contest = repo.get_repo(ContestRepo)




