from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Указываем тип бд(postgres, sqlite)
SQL_DATABASE = "sqlite:///./test.db"

# Создаем движок
engine = create_engine(SQL_DATABASE)

# Создаем сессию что бы хранить данные
SessionLocal = sessionmaker(bind=engine)

# Создаем полнаценную базу
Base = declarative_base()


# Функция для подключения к бд
def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()