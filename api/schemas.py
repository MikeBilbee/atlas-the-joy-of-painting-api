from pydantic import BaseModel
from typing import List


class ColorBase(BaseModel):
    color_name: str
    color_hex: str

class Color(ColorBase):
    color_id: int
    class Config:
        orm_mode = True

class SubjectBase(BaseModel):
    subject_name: str

class Subject(SubjectBase):
    subject_id: int
    class Config:
        orm_mode = True
    
class EpisodeBase(BaseModel):
    episode_name: str
    air_date: str  

class Episode(EpisodeBase):
    episode_id: int
    colors: List[Color] = []
    subjects: List[Subject] = []

    class Config:
        orm_mode = True
        