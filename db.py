from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from settings import settings

# Base model class (SQLAlchemy 2.0)
class Base(DeclarativeBase):
    pass


# Get connection string safely
DATABASE_URL = settings.DATABASE_URL.get_secret_value()

# Create engine
engine = create_engine(
    DATABASE_URL,
    echo=False,          # Turn on in development if needed
    future=True,         # SQLAlchemy 2.0 style
    pool_pre_ping=True,  # Reconnect on dead connection
)

# Session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    future=True,
)


# Dependency for FastAPI routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
