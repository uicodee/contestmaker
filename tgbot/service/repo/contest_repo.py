from sqlalchemy import insert, select, update

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
        sql = select(self.model)
        request = await self._session.execute(sql)
        contests = request.scalars().all()
        return contests

    async def update_status(self, contest_id: int, finished: bool):
        sql = update(self.model).where(self.model.id == contest_id).values({'finished': finished})
        await self._session.execute(sql)
        await self._session.commit()
