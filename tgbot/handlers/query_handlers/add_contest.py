from aiogram import types

from tgbot.data.strings import get_contest_name, cancel, main_menu_btn
from tgbot.states.states import ContestForm


async def add_contest(query: types.CallbackQuery):
    await query.message.edit_text(
        text=get_contest_name,
        reply_markup=types.InlineKeyboardMarkup(
            row_width=1,
            inline_keyboard=[
                [types.InlineKeyboardButton(text=cancel, callback_data='cancel')],
                [types.InlineKeyboardButton(text=main_menu_btn, callback_data='main_menu')]
            ]
        )
    )
    await ContestForm.name.set()
