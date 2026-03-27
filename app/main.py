from fastapi import FastAPI
from app.api.routes import router
from app.db.database import Base, engine

app = FastAPI(title="URL Shortener")

Base.metadata.create_all(bind=engine)

app.include_router(router)