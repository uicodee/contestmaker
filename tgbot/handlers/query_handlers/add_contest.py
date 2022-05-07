from aiogram import types

from tgbot.states.states import ContestForm


async def add_contest(query: types.CallbackQuery):
    await query.message.edit_text(
        text='Konkurs nomini kiriting',
        reply_markup=types.InlineKeyboardMarkup(
            row_width=1,
            inline_keyboard=[
                [types.InlineKeyboardButton(text='Bekor qilish', callback_data='cancel')]
            ]
        )
    )
    await ContestForm.name.set()
