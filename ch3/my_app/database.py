import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = os.getenv(
    key="SQLALCHEMY_DATABASE_URL",
    default="postgresql://userforapi:pwforapi@localhost:5432/dbforapi",
)

# Create engine
engine = create_engine(url=SQLALCHEMY_DATABASE_URL)

# Create class of database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for ORM models
Base = declarative_base()