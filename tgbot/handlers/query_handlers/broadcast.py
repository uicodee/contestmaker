import asyncio
import datetime

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.utils import exceptions

from tgbot.config import Config
from tgbot.data.strings import broadcast_message, main_menu_btn, stats_broadcast
from tgbot.service.repo.repository import SQLAlchemyRepos
from tgbot.service.repo.user_repo import UserRepo
from tgbot.states.states import BroadcastForm


async def alert_broadcast(query: types.CallbackQuery):
    await query.message.edit_text(
        text=broadcast_message,
        reply_markup=types.InlineKeyboardMarkup(
            row_width=1,
            inline_keyboard=[
                [types.InlineKeyboardButton(text=main_menu_btn, callback_data='main_menu')]
            ]
        )
    )
    await BroadcastForm.content.set()


async def broadcast(query: types.CallbackQuery, repo: SQLAlchemyRepos, state: FSMContext):
    config: Config = query.message.bot.get('config')
    start_time = datetime.datetime.utcnow()
    msg: types.Message = (await state.get_data()).get('msg')
    users = await repo.get_repo(UserRepo).get_users()
    delivered = 0
    undelivered = 0
    for user in users:
        try:
            if user.user_id != config.tg_bot.admin_id:
                await query.message.bot.copy_message(
                    chat_id=user.user_id,
                    from_chat_id=query.message.chat.id,
                    message_id=msg.message_id
                )
                delivered += 1
        except exceptions.BotBlocked:
            undelivered += 1
        except exceptions.ChatNotFound:
            undelivered += 1
        except exceptions.RetryAfter as e:
            await asyncio.sleep(e.timeout)
            await query.message.bot.copy_message(
                chat_id=user.user_id,
                from_chat_id=query.message.chat.id,
                message_id=msg.message_id
            )
        except exceptions.UserDeactivated:
            undelivered += 1
        except exceptions.TelegramAPIError:
            undelivered += 1
    end_time = datetime.datetime.utcnow()
    await query.message.edit_text(
        text=stats_broadcast.format(
            delivered=delivered,
            undelivered=undelivered,
            time=end_time-start_time
        )
    )
