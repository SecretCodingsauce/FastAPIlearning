# tests/database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import settings


test_engine = create_engine(settings.test_database_url)

TestingSessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=test_engine
)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()