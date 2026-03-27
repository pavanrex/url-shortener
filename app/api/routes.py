from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from app.services.url_service import shorten_url, get_original_url

router = APIRouter()

@router.post("/shorten")
def create_short_url(long_url: str):
    return {"short_url": shorten_url(long_url)}

@router.get("/{short_id}")
def redirect(short_id: str):
    url = get_original_url(short_id)
    if url:
        return RedirectResponse(url=url)
    return {"error": "URL not found"}