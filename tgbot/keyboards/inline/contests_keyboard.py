from aiogram import types

from tgbot.callback_datas.callback_datas import cb_contest_delete, cb_contest_view
from tgbot.models import Contest


def contests_list_keyboard(contests: list[Contest]) -> types.InlineKeyboardMarkup:
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    for contest in contests:
        keyboard.add(
            types.InlineKeyboardButton(text=contest.name, callback_data=cb_contest_view.new(contest_id=contest.id)),
            types.InlineKeyboardButton(text="🗑", callback_data=cb_contest_delete.new(contest_id=contest.id)),
        )

    return keyboard
