from sqlalchemy import Column, Integer, String
from .db_session import SqlAlchemyBase


class User(SqlAlchemyBase):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)  # Id модуля(+)
    name = Column(String(250), nullable=False)  # ФИО(+)
    mail = Column(String(250), nullable=False)  # почта пользователя(+)
    phone = Column(String(250), nullable=False)  # Телефон пользователя(+)
    login = Column(String(250), nullable=False)  # Логин пользователя(+)
    password = Column(String(200), nullable=False)  # Пароль пользователя(+)
    code_password = Column(String(200), nullable=False)  # Код пользователя(+)
