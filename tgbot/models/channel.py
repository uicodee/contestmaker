from sqlalchemy import Column, BigInteger, String

from tgbot.models import BaseModel


class Channel(BaseModel):
    __tablename__ = 'channels'

    id = Column(BigInteger(), autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(length=100), nullable=False)
    link = Column(String(length=100), nullable=False)

    def __repr__(self):
        return f'{self.link}'
