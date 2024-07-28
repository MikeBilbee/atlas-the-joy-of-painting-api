""" Initiates the Database for use """
from engine.db import SessionLocal
# Pretty sure this variable name is imported so "Session" can be used in views
from sqlalchemy.orm import Session
from typing import Generator


def get_db() -> Generator:
    """ Create db session"""
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
