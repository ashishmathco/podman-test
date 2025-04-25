from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db import session, models
from api import routes

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

models.Base.metadata.create_all(bind=session.engine)
app.include_router(routes.router)