from aiogram.types import Message

from tgbot.data.strings import welcome_admin
from tgbot.keyboards.inline.admin_panel import admin_panel


async def admin_start(message: Message):
    await message.answer(
        text=welcome_admin,
        reply_markup=admin_panel()
    )



    # # or you can pass multiple roles:
    # dp.register_message_handler(admin_start, commands=["start"], state="*", role=[UserRole.ADMIN])
    # # or use another filter:
    # dp.register_message_handler(admin_start, commands=["start"], state="*", is_admin=True)
