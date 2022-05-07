from aiogram import Dispatcher

from .add_channel import add_channel
from .cancel import cancel
from .add import add
from .channels_list import channels_list
from .channel_actions import delete_channel, view_channel
from .check_subscription import check_subscription
from .add_contest import add_contest
from .contests_list import contests_list

from tgbot.callback_datas.callback_datas import cb_channel_view, cb_channel_delete
from tgbot.states.states import ChannelForm


def register_query_handler(dp: Dispatcher):
    dp.register_callback_query_handler(add_channel, text='add_channel', state=None)
    dp.register_callback_query_handler(add, text='add', state=ChannelForm.link)
    dp.register_callback_query_handler(check_subscription, text='check_subscription')
    dp.register_callback_query_handler(channels_list, text='channels_list', state=None)
    dp.register_callback_query_handler(delete_channel, cb_channel_delete.filter())
    dp.register_callback_query_handler(view_channel, cb_channel_view.filter())
    dp.register_callback_query_handler(add_contest, text='add_contest')
    dp.register_callback_query_handler(contests_list, text='contests_list')
    dp.register_callback_query_handler(cancel, text='cancel', state="*")
