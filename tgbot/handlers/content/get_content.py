from aiogram import types
from aiogram.dispatcher import FSMContext

from tgbot.data.strings import confirm, cancel
from tgbot.service.repo.repository import SQLAlchemyRepos


async def get_content(message: types.Message, state: FSMContext):
    msg = await message.bot.copy_message(
        chat_id=message.chat.id,
        from_chat_id=message.chat.id,
        message_id=message.message_id,
        reply_markup=types.InlineKeyboardMarkup(
            row_width=1,
            inline_keyboard=[
                [types.InlineKeyboardButton(text=confirm, callback_data='start_broadcast')],
                [types.InlineKeyboardButton(text=cancel, callback_data='cancel')],
            ]
        )
    )
    await state.update_data(msg=msg)
    await state.reset_state(with_data=False)
