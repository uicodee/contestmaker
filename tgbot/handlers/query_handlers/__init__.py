from aiogram import Dispatcher

from .add_channel import add_channel
from .cancel import cancel, main_menu
from .add import add
from .channels_list import channels_list
from .channel_actions import delete_channel, view_channel
from .check_subscription import check_subscription
from .add_contest import add_contest
from .contests_list import contests_list
from .contest_actions import delete_contest, view_contest, back_contest
from .random import random, select_contest, select_count_winners, start_randomise


from tgbot.callback_datas.callback_datas import (
    cb_channel_view,
    cb_channel_delete,
    cb_contest_view,
    cb_contest_delete,
    cb_select_count, cb_select_contest
)
from tgbot.states.states import ChannelForm, RandomForm


def register_query_handler(dp: Dispatcher):
    dp.register_callback_query_handler(add_channel, text='add_channel', state=None)
    dp.register_callback_query_handler(add, text='add', state=ChannelForm.link)
    dp.register_callback_query_handler(check_subscription, text='check_subscription')
    dp.register_callback_query_handler(channels_list, text='channels_list', state=None)
    dp.register_callback_query_handler(delete_channel, cb_channel_delete.filter())
    dp.register_callback_query_handler(view_channel, cb_channel_view.filter())
    dp.register_callback_query_handler(add_contest, text='add_contest')
    dp.register_callback_query_handler(contests_list, text='contests_list')
    dp.register_callback_query_handler(delete_contest, cb_contest_delete.filter())
    dp.register_callback_query_handler(view_contest, cb_contest_view.filter())
    dp.register_callback_query_handler(back_contest, text='back_contest')
    dp.register_callback_query_handler(random, text='random')
    dp.register_callback_query_handler(select_contest, cb_select_contest.filter(), state=RandomForm.contest_id)
    dp.register_callback_query_handler(select_count_winners, cb_select_count.filter(), state=RandomForm.winners)
    dp.register_callback_query_handler(start_randomise, text='start_random')

    dp.register_callback_query_handler(main_menu, text='main_menu', state="*")
    dp.register_callback_query_handler(cancel, text='cancel', state="*")
