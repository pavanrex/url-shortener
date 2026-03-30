import string
import random
from sqlalchemy.orm import Session
from app.models.url import URL
from app.core.redis import redis_client


# 🔹 Generate short ID
def generate_short_id(length: int = 6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


# 🔹 Create short URL
def shorten_url(db: Session, long_url: str):
    short_id = generate_short_id()

    url = URL(
        short_id=short_id,
        long_url=long_url
    )

    db.add(url)
    db.commit()
    db.refresh(url)

    return url


# 🔹 Get original URL (with Redis caching + click tracking)
def get_original_url(db: Session, short_id: str):

    # 1️⃣ Check Redis cache
    cached_url = redis_client.get(short_id)
    if cached_url:
        return cached_url

    # 2️⃣ Fetch from DB
    url = db.query(URL).filter(URL.short_id == short_id).first()

    if url:
        # increment clicks
        url.clicks += 1
        db.commit()

        # 3️⃣ Store in Redis (1 hour expiry)
        redis_client.setex(short_id, 3600, url.long_url)

        return url.long_url

    return None