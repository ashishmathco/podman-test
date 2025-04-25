from fastapi import APIRouter
from db import crud

router = APIRouter()

@router.get("/")
def root():
    return {"message": "Hello from FastAPI"}

@router.get("/items/")
def get_items():
    return crud.get_items()

@router.post("/items/")
def create_item(name: str):
    return crud.create_item(name)