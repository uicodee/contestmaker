from aiogram.dispatcher.filters.state import StatesGroup, State


class ChannelForm(StatesGroup):
    name = State()
    link = State()


class ContestForm(StatesGroup):
    name = State()


class RandomForm(StatesGroup):
    contest_id = State()
    winners = State()


class BroadcastForm(StatesGroup):
    content = State()

