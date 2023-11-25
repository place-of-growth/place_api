from sqlalchemy import Column, Integer, String
from .db_session import SqlAlchemyBase


class Events(SqlAlchemyBase):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True)  # id мероприятия(+)
    title_event = Column(String(250), nullable=False)  # Название мероприятия(+)
    description_event = Column(String(250), nullable=False)  # Описание мероприятия(+)
    photo_event = Column(String(250))  # Фото мероприятия
