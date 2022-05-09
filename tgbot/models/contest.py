from sqlalchemy import Column, BigInteger, String, Boolean

from tgbot.models import BaseModel


class Contest(BaseModel):
    __tablename__ = 'contests'

    id = Column(BigInteger(), autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(length=300), nullable=False)
    finished = Column(Boolean(), nullable=False)

    def __repr__(self):
        return f'{self.id} | {self.name}'
