from aiogram.dispatcher.filters.state import StatesGroup, State


class ChannelForm(StatesGroup):
    name = State()
    link = State()


class ContestForm(StatesGroup):
    name = State()
