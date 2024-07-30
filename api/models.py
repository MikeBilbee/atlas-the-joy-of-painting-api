from engine.db import Base
from sqlalchemy import Column, Integer, String


class Episode(Base):
    """ episodes table inherits from declarative base to define columns """
    __tablename__ = 'episodes'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(50), nullable=False, unique=True)
    date = Column(String(20), nullable=False, unique=True)
    color_list = Column(String(200), nullable=False)
    subject_list = Column(String(200), nullable=False)

    def __repr__(self):
        """ Return string representation of object """
        return f'<Episode {self.title}>'