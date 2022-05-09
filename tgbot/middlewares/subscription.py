from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware

from tgbot.data.strings import subscribe_alert, welcome_user_channel
from tgbot.keyboards.inline.channels_keyboard import channels_keyboard
from tgbot.service.repo.channel_repo import ChannelRepo
from tgbot.service.repo.repository import SQLAlchemyRepos


class Subscription(BaseMiddleware):

    async def on_pre_process_message(self, message: types.Message, data: dict):
        repo: SQLAlchemyRepos = data.get('repo')
        channel = repo.get_repo(ChannelRepo)
        channels = await channel.get_channels()
        statuses = []
        for ch in channels:
            status = await message.bot.get_chat_member(
                chat_id=ch.link,
                user_id=message.from_user.id
            )
            statuses.append(status.status)
        if 'left' in statuses:
            await message.answer(
                text=welcome_user_channel,
                reply_markup=channels_keyboard(channels=channels)
            )
            raise CancelHandler()
