import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session
import sqlalchemy.ext.declarative as dec

SqlAlchemyBase = dec.declarative_base()

__factory = None


def global_init():
    global __factory

    if __factory:
        return

    # if not db_file or not db_file.strip():
    #     raise Exception("Необходимо указать файл базы данных.")

    conn_str = f'sqlite:///models/place.db'
    print(f"Подключение к базе данных по адресу {conn_str}")

    engine = sa.create_engine(conn_str, echo=False)
    # engine = sa.create_engine(conn_str, echo=False, connect_args={'connect_timeout': 20})
    __factory = orm.sessionmaker(bind=engine)

    from . import __all_models

    SqlAlchemyBase.metadata.create_all(engine)
    print('Таблицы инициализированы')


def create_session() -> Session:
    global __factory
    return __factory()
