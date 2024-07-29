from sqlalchemy import Column, Integer, String, Date, Table, ForeignKey
from sqlalchemy.orm import relationship
from engine.db import Base

class Episode(Base):
    __tablename__ = "episodes"

    episode_id = Column(Integer, primary_key=True, index=True)
    episode_name = Column(String, unique=True, index=True)
    air_date = Column(Date)
    colors = relationship("Color", secondary="episode_colors", back_populates="episodes")
    subjects = relationship("Subject", secondary="episode_subjects", back_populates="episodes")

class Color(Base):
    __tablename__ = "colors"

    color_id = Column(Integer, primary_key=True, index=True)
    color_name = Column(String, unique=True, index=True)
    color_hex = Column(String, unique=True, index=True)
    episodes = relationship("Episode", secondary="episode_colors", back_populates="colors")

class Subject(Base):
    __tablename__ = "subjects"

    subject_id = Column(Integer, primary_key=True, index=True)
    subject_name = Column(String, unique=True, index=True)
    episodes = relationship("Episode", secondary="episode_subjects", back_populates="subjects")

episode_colors = Table(
    "episode_colors",
    Base.metadata,
    Column("episode_id", Integer, ForeignKey("episodes.episode_id")),
    Column("color_id", Integer, ForeignKey("colors.color_id")),
)

episode_subjects = Table(
    "episode_subjects",
    Base.metadata,
    Column("episode_id", Integer, ForeignKey("episodes.episode_id")),
    Column("subject_id", Integer, ForeignKey("subjects.subject_id")),
)
