from aiogram import types
from aiogram.dispatcher import FSMContext

from tgbot.data.strings import welcome_admin, cancelled
from tgbot.keyboards.inline.admin_panel import admin_panel


async def cancel(query: types.CallbackQuery, state: FSMContext):
    await state.reset_state(with_data=True)
    await query.message.delete()
    await query.answer(text=cancelled)


async def main_menu(query: types.CallbackQuery, state: FSMContext):
    await state.reset_state(with_data=True)
    await query.message.edit_text(
        text=welcome_admin,
        reply_markup=admin_panel()
    )
