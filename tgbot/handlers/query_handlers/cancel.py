from aiogram import types
from aiogram.dispatcher import FSMContext


async def cancel(query: types.CallbackQuery, state: FSMContext):
    await state.reset_state(with_data=True)
    await query.message.delete()
    await query.answer(text='Bekor qilindi')
