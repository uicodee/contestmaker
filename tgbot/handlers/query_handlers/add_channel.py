from aiogram import types

from tgbot.states.states import ChannelForm


async def add_channel(query: types.CallbackQuery):
    await query.message.edit_text(
        text='Kanal nomini kiriting',
        reply_markup=types.InlineKeyboardMarkup(
            row_width=1,
            inline_keyboard=[
                [types.InlineKeyboardButton(text='Bekor qilish', callback_data='cancel')]
            ]
        )
    )
    await ChannelForm.name.set()
