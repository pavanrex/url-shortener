from fastapi import APIRouter, Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from app.services.url_service import shorten_url, get_original_url
from app.db.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/shorten")
def create_short_url(long_url: str, db: Session = Depends(get_db)):
    return {"short_url": shorten_url(db, long_url)}

@router.get("/{short_id}")
def redirect(short_id: str, db: Session = Depends(get_db)):
    url = get_original_url(db, short_id)
    if url:
        return RedirectResponse(url=url)
    return {"error": "URL not found"}