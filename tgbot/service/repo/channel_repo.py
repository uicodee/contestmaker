from sqlalchemy import insert, select, delete
from tgbot.models.channel import Channel
from tgbot.service.repo.base_repo import BaseSQLAlchemyRepo


class ChannelRepo(BaseSQLAlchemyRepo):
    model = Channel

    async def get_channels(self) -> list[Channel]:
        sql = select(self.model)
        request = await self._session.execute(sql)
        channels = request.scalars().all()
        return channels

    async def add_channel(self, name: str, link: str):
        sql = insert(self.model).values(name=name, link=link).returning("*")
        await self._session.execute(sql)
        await self._session.commit()

    async def get_channel(self, channel_id: int) -> model:
        sql = select(self.model).filter(self.model.id == channel_id)
        request = await self._session.execute(sql)
        return request.scalar()

    async def delete_channel(self, channel_id: int):
        sql = delete(self.model).filter(self.model.id == channel_id)
        await self._session.execute(sql)
        await self._session.commit()
