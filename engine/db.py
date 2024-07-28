""" Creates a New Database"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Create New DB
SQLALCHEMY_DATEBASE_URI = 'sqlite:///joy_of_painting.db'

# Create Engine
engine = create_engine(SQLALCHEMY_DATEBASE_URI)
# Create New Session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
