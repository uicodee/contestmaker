from sqlalchemy import Column, BigInteger, String, Boolean

from tgbot.models import BaseModel


class ContestUser(BaseModel):
    __tablename__ = 'contests_users'

    id = Column(BigInteger(), autoincrement=True, nullable=False, primary_key=True)
    user_id = Column(BigInteger, nullable=False, autoincrement=False, primary_key=True)
    contest_id = Column(BigInteger, nullable=False, autoincrement=False, primary_key=True)

    def __repr__(self):
        return f'{self.id} | {self.user_id} | {self.contest_id}'
