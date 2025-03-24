from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.core.schemas.theme import Theme
from app.db.session import get_db
from app.services import theme_service

router = APIRouter()

@router.post("/", response_model=Theme, tags=["Themes"])
def create_theme(theme: Theme, db: Session = Depends(get_db)):
    return theme_service.create_theme(db, theme)

@router.get("/", response_model=list[Theme], tags=["Themes"])
def get_themes(db: Session = Depends(get_db)):
    return theme_service.get_themes(db)

@router.get("/{theme_id}", response_model=Theme, tags=["Themes"])
def get_theme(theme_id: int, db: Session = Depends(get_db)):
    return theme_service.get_theme(db, theme_id)

@router.put("/{theme_id}", response_model=Theme, tags=["Themes"])
def update_theme(theme_id: int, theme: Theme, db: Session = Depends(get_db)):
    return theme_service.update_theme(db, theme_id, theme)

@router.delete("/{theme_id}", tags=["Themes"], status_code=204)
def delete_theme(theme_id: int, db: Session = Depends(get_db)):
    theme_service.delete_theme(db, theme_id)
