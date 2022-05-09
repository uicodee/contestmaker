from aiogram import types
from aiogram.dispatcher import FSMContext

from tgbot.data.strings import send_link_admin, cancel, check_data_channel, confirm
from tgbot.states.states import ChannelForm


async def get_name(message: types.Message, state: FSMContext):
    name = message.text
    await message.answer(
        text=send_link_admin,
        reply_markup=types.InlineKeyboardMarkup(
            row_width=1,
            inline_keyboard=[
                [types.InlineKeyboardButton(text=cancel, callback_data='cancel')]
            ]
        )
    )
    await ChannelForm.link.set()
    await state.update_data(name=name)


async def get_link(message: types.Message, state: FSMContext):
    data = await state.get_data()
    link = message.text
    if link.startswith('https'):
        channel_link = "@" + link.split('/')[-1]
    elif link.startswith('@'):
        channel_link = link
    else:
        channel_link = f'@{link}'
    await state.update_data(link=channel_link)
    await message.answer(
        text=check_data_channel.format(channel=data.get("name"), link=link),
        reply_markup=types.InlineKeyboardMarkup(
            row_width=1,
            inline_keyboard=[
                [types.InlineKeyboardButton(text=confirm, callback_data='add')],
                [types.InlineKeyboardButton(text=cancel, callback_data='cancel')],
            ]
        )
    )
