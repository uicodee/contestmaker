from aiogram import Dispatcher
from .get_channel import get_name, get_link
from .get_contest import get_contest_name
from .get_content import get_content

from tgbot.states.states import ChannelForm, ContestForm, BroadcastForm


def register_content(dp: Dispatcher):
    dp.register_message_handler(get_name, state=ChannelForm.name)
    dp.register_message_handler(get_link, state=ChannelForm.link)
    dp.register_message_handler(get_contest_name, state=ContestForm.name)
    dp.register_message_handler(get_content, state=BroadcastForm.content)
