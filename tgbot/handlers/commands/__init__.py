import re

from aiogram import types

from aiogram import Dispatcher
from aiogram.dispatcher.filters import CommandStart, Command

from .user import user_start, referral_start, contest_start
from .admin import admin_start
from tgbot.models.role import UserRole


def register_user(dp: Dispatcher):
    dp.register_message_handler(referral_start, CommandStart(re.compile(r'^\d+$')), state="*")
    dp.register_message_handler(contest_start, CommandStart(re.compile(r'contest_\d')), state="*")
    dp.register_message_handler(user_start, commands=["start"], state="*")


def register_admin(dp: Dispatcher):
    dp.register_message_handler(admin_start, commands=["admin"], state="*", role=UserRole.ADMIN)
