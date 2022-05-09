from sqlalchemy import insert, select, and_

from tgbot.models.contest_user import ContestUser
from tgbot.service.repo.base_repo import BaseSQLAlchemyRepo
from sqlalchemy import func


class ContestUserRepo(BaseSQLAlchemyRepo):
    model = ContestUser

    async def add_contest_user(self, user_id: int, contest_id: int):
        sql = insert(self.model).values(user_id=user_id, contest_id=contest_id)
        await self._session.execute(sql)
        await self._session.commit()

    async def get_user_contest(self, user_id: int, contest_id: int):
        sql = select(self.model).filter(self.model.user_id == user_id, self.model.contest_id == contest_id)
        request = await self._session.execute(sql)
        user = request.scalar()
        return user

    async def get_contest_users(self, contest_id: int):
        sql = select(self.model).filter(self.model.contest_id == contest_id)
        request = await self._session.execute(sql)
        return request.scalars().all()

    async def select_random_user(self, contest_id: int, winners: int) -> list[model]:
        sql = select(self.model).filter(self.model.contest_id == contest_id).order_by(func.random()).limit(winners)
        request = await self._session.execute(sql)
        return request.scalars().all()

    # async def get_contest(self) -> list[model]:
    #     sql = select(self.model).filter(self.model.finished == False)
    #     request = await self._session.execute(sql)
    #     contests = request.scalars().all()
    #     return contests
    #
    # async def delete_cont(self, contest_id: int):
    #     sql = delete(self.model).filter(self.model.id == contest_id)
    #     await self._session.execute(sql)
    #     await self._session.commit()
    #
    # async def update_status(self, contest_id: int, finished: bool):
    #     sql = update(self.model).where(self.model.id == contest_id).values({'finished': finished})
    #     await self._session.execute(sql)
    #     await self._session.commit()
    #
    # async def get_contest_id(self, contest_id: int) -> model:
    #     sql = select(self.model).filter(self.model.id == contest_id)
    #     request = await self._session.execute(sql)
    #     return request.scalar()
