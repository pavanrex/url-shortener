from fastapi import FastAPI
from app.api.routes import router
from app.db.database import Base, engine
from app.models import url

app = FastAPI(title="URL Shortener")

Base.metadata.create_all(bind=engine)

app.include_router(router)