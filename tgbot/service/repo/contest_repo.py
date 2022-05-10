from sqlalchemy import insert, select, update, delete

from tgbot.models import Contest
from tgbot.service.repo.base_repo import BaseSQLAlchemyRepo


class ContestRepo(BaseSQLAlchemyRepo):
    model = Contest

    async def add_contest(self, name: str):
        sql = insert(self.model).values(name=name, finished=False).returning(self.model.id)
        request = await self._session.execute(sql)
        await self._session.commit()
        return request.scalar()

    async def get_contest(self) -> list[model]:
        sql = select(self.model).filter(self.model.finished == False)
        request = await self._session.execute(sql)
        contests = request.scalars().all()
        return contests

    async def get_contest_finished(self) -> list[model]:
        sql = select(self.model).filter(self.model.finished == True)
        request = await self._session.execute(sql)
        contests = request.scalars().all()
        return contests

    async def delete_cont(self, contest_id: int):
        sql = delete(self.model).filter(self.model.id == contest_id)
        await self._session.execute(sql)
        await self._session.commit()

    async def update_status(self, contest_id: int, finished: bool):
        sql = update(self.model).where(self.model.id == contest_id).values({'finished': finished})
        await self._session.execute(sql)
        await self._session.commit()

    async def get_contest_id(self, contest_id: int) -> model:
        sql = select(self.model).filter(self.model.id == contest_id)
        request = await self._session.execute(sql)
        return request.scalar()
