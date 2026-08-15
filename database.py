from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Для SQLite используем локальный файл
# Можно также использовать :memory: для временной БД в памяти
SQL_DB_URL = "sqlite:///./app.db"  # или "sqlite:///:memory:" для временной

# Для SQLite нужно добавить параметр для поддержки внешних ключей
engine = create_engine(
    SQL_DB_URL, 
    connect_args={"check_same_thread": False}  # нужно для многопоточности
)

session_local = sessionmaker(autoflush=False, autocommit=False, bind=engine)
Base = declarative_base()