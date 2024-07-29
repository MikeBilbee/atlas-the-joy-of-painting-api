from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
from initiate import get_db
from api.models import Episode, Color, Subject
from api.schemas import Episode as EpisodeSchema, Color as ColorSchema, Subject as SubjectSchema

router = APIRouter()

@router.get("/episodes/", response_model=List[EpisodeSchema])
def read_episodes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    episodes = db.query(Episode).offset(skip).limit(limit).all()
    for episode in episodes:
        episode.colors = [color.color_name for color in episode.colors]
        episode.subjects = [subject.subject_name for subject in episode.subjects]
    return episodes

@router.get("/episodes/{episode_id}", response_model=EpisodeSchema)
def read_episode(episode_id: int, db: Session = Depends(get_db)):
    episode = db.query(Episode).filter(Episode.episode_id == episode_id).first()
    if episode is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Episode not found")
    episode.colors = [color.color_name for color in episode.colors]
    episode.subjects = [subject.subject_name for subject in episode.subjects]
    return episode

@router.get("/colors/", response_model=List[ColorSchema])
def read_colors(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    colors = db.query(Color).offset(skip).limit(limit).all()
    return colors

@router.get("/colors/{color_id}", response_model=ColorSchema)
def read_color(color_id: int, db: Session = Depends(get_db)):
    color = db.query(Color).filter(Color.color_id == color_id).first()
    if color is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Color not found")
    return color

@router.get("/subjects/", response_model=List[SubjectSchema])
def read_subjects(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    subjects = db.query(Subject).offset(skip).limit(limit).all()
    return subjects

@router.get("/subjects/{subject_id}", response_model=SubjectSchema)
def read_subject(subject_id: int, db: Session = Depends(get_db)):
    subject = db.query(Subject).filter(Subject.subject_id == subject_id).first()
    if subject is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Subject not found")
    return subject