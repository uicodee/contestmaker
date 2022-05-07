from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

from tgbot.states.states import ChannelForm


async def get_name(message: types.Message, state: FSMContext):
    name = message.text
    await message.answer(
        text='Endi esa kanal link (havolasini) yuboring',
        reply_markup=types.InlineKeyboardMarkup(
            row_width=1,
            inline_keyboard=[
                [types.InlineKeyboardButton(text='Bekor qilish', callback_data='cancel')]
            ]
        )
    )
    await ChannelForm.link.set()
    await state.update_data(name=name)


async def get_link(message: types.Message, state: FSMContext):
    data = await state.get_data()
    link = message.text
    if link.startswith('https'):
        channel_link = link.split('/')[-1]
    elif link.startswith('@'):
        channel_link = link
    else:
        channel_link = f'@{link}'
    await state.update_data(link=channel_link)
    await message.answer(
        text='Ma\'lumotlarni qayta tekshirib oling:\n'
             f'Kanal nomi: {data.get("name")}\n'
             f'Kanal havolasi: {link}',
        reply_markup=types.InlineKeyboardMarkup(
            row_width=1,
            inline_keyboard=[
                [types.InlineKeyboardButton(text='Tasdiqlash', callback_data='add')],
                [types.InlineKeyboardButton(text='Bekor qilish', callback_data='cancel')],
            ]
        )
    )
