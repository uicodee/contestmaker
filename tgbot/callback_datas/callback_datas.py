from aiogram.utils.callback_data import CallbackData


cb_channel_view = CallbackData("view_channel", "channel_id")
cb_channel_delete = CallbackData("delete_channel", "channel_id")
cb_contest_view = CallbackData("view_contest", "contest_id")
cb_contest_delete = CallbackData("delete_contest", "contest_id")
cb_select_contest = CallbackData("select", "contest_id")
cb_select_count = CallbackData("select_count", "count")
