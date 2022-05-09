from aiogram import Dispatcher
from .cabinet import my_cabinet
from ...data.strings import cabinet_text


def register_buttons(dp: Dispatcher):
    dp.register_message_handler(my_cabinet, text=cabinet_text, state="*")
