from tgbot.models import BaseModel
from sqlalchemy import Column, BigInteger, String, Boolean


class Referral(BaseModel):
    __tablename__ = 'referral'

    user_id = Column(BigInteger, nullable=False, autoincrement=False, primary_key=True)
    referrer_id = Column(BigInteger, nullable=False, autoincrement=False, primary_key=True)
    name = Column(String(length=60), nullable=False)
    username = Column(String(length=100), nullable=True)

    def __repr__(self):
        return f'{self.user_id} | {self.name} | {self.username}'
