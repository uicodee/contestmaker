from aiogram import Dispatcher

from .user import user_start
from .admin import admin_start
from ...models.role import UserRole


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")


def register_admin(dp: Dispatcher):
    dp.register_message_handler(admin_start, commands=["admin"], state="*", role=UserRole.ADMIN)
