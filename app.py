""" Driver program for application """
from api import models, endpoints
from engine.db import engine, sessionmaker
from fastapi import FastAPI


models.Base.metadata.create_all(bind=engine)
sessionmaker = sessionmaker(bind=engine)
session = sessionmaker()

# Create new FastAPI instance
app = FastAPI()

# Bind routes to views as seen in api/v1/episodes/views.py
app.include_router(endpoints.router)