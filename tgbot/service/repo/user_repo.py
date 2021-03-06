import datetime

from sqlalchemy import insert, select, update, func

from tgbot.models.user import User
from tgbot.service.repo.base_repo import BaseSQLAlchemyRepo


class UserRepo(BaseSQLAlchemyRepo):
    model = User

    async def add_user(self, user_id: int, name: str, subscribed: bool, referrals: int, username: str):
        sql = insert(self.model).values(
            user_id=user_id,
            name=name,
            username=username,
            subscribed=subscribed,
            referrals=referrals
        ).returning('*')
        await self._session.execute(sql)
        await self._session.commit()

    async def get_user(self, user_id: int) -> model:
        sql = select(self.model).where(self.model.user_id == user_id)
        request = await self._session.execute(sql)
        user = request.scalar()
        return user

    async def get_users(self) -> model:
        sql = select(self.model)
        request = await self._session.execute(sql)
        user = request.scalars().all()
        return user

    async def update_status(self, user_id: int, subscribed: bool):
        sql = update(self.model).where(self.model.user_id == user_id).values({'subscribed': subscribed})
        await self._session.execute(sql)
        await self._session.commit()

    async def increase_referrals(self, user_id: int, count: int):
        result = await self._session.execute(select(self.model.referrals).filter(self.model.user_id == user_id))
        sql = update(self.model).where(self.model.user_id == user_id).values(
            {"referrals": int(result.scalar()) + count})
        await self._session.execute(sql)
        await self._session.commit()

    async def count_user(self):
        sql = select(func.count()).select_from(self.model)
        request = await self._session.execute(sql)
        return request.scalar()

    async def today_users(self, date: datetime.datetime):
        sql = select(func.count()).select_from(self.model).where(self.model.created_at == date)
        request = await self._session.execute(sql)
        return request.scalar()
