from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///cherepaha.db')
Base = declarative_base()


class User(Base):
    """Данный класс является моделью, которая описывает структуру данных для пользователей в базе данных cherepaha.db.
       Наследуется от Base, который создаётся при помощи функции declarative_base(),
       что позволяет использовать функциональность, предоставляемую SQLAlchemy, для работы с базами данных"""

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    last_name = Column(String(100), nullable=False)
    first_name = Column(String(100), nullable=False)
    patronymic = Column(String(100), nullable=False)
    phone_number = Column(String(15), nullable=True)
    email = Column(String(254), nullable=False)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
