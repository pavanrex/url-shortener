import string
import random
from sqlalchemy.orm import Session
from app.models.url import URL

def generate_id(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def shorten_url(db: Session, long_url: str):
    while True:
        short_id = generate_id()
        existing = db.query(URL).filter(URL.short_id == short_id).first()
        if not existing:
            break

    new_url = URL(short_id=short_id, long_url=long_url)
    db.add(new_url)
    db.commit()
    db.refresh(new_url)

    return f"http://localhost:8000/{short_id}"

def get_original_url(db: Session, short_id: str):
    url = db.query(URL).filter(URL.short_id == short_id).first()
    return url.long_url if url else None