from sqlalchemy import insert, select, update

from tgbot.models.referral import Referral
from tgbot.service.repo.base_repo import BaseSQLAlchemyRepo


class ReferralsRepo(BaseSQLAlchemyRepo):
    model = Referral

    async def add_referral(self, user_id: int, referrer_id: int, name: str, username: str):
        sql = insert(self.model).values(
            user_id=user_id,
            referrer_id=referrer_id,
            name=name,
            username=username
        )
        await self._session.execute(sql)
        await self._session.commit()

    async def get_referral(self, user_id: int):
        sql = select(self.model).filter(self.model.user_id == user_id)
        request = await self._session.execute(sql)
        return request.scalar()
