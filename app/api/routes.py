from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

from app.db.database import get_db
from app.models.url import URL
from app.services.url_service import shorten_url, get_original_url

router = APIRouter()


# 🔹 Create short URL
@router.post("/shorten")
def create_short_url(long_url: str, db: Session = Depends(get_db)):
    return shorten_url(db, long_url)


# 🔹 Redirect
@router.get("/{short_id}")
def redirect(short_id: str, db: Session = Depends(get_db)):
    url = get_original_url(db, short_id)
    if url:
        return RedirectResponse(url=url)
    raise HTTPException(status_code=404, detail="URL not found")


# 🔹 Stats
@router.get("/stats/{short_id}")
def get_stats(short_id: str, db: Session = Depends(get_db)):
    url = db.query(URL).filter(URL.short_id == short_id).first()

    if not url:
        raise HTTPException(status_code=404, detail="URL not found")

    return {
        "short_id": url.short_id,
        "long_url": url.long_url,
        "clicks": url.clicks,
        "created_at": str(url.created_at)
    }