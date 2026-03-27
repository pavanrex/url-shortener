# URL Shortener (Bitly-style)

A scalable backend system that converts long URLs into short, shareable links with persistent storage.

## Features

- Generate short URLs from long URLs
- Redirect users to original URLs
- Persistent storage using SQLite
- Collision-resistant ID generation
- Modular backend architecture (API, services, models)

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite

## Project Structure
- app/
- api/ # Routes
- services/ # Business logic
- models/ # Database models
- db/ # DB connection


## How to Run
- bash   
- git clone https://github.com/pavanrex/url-shortener.git
- cd url-shortener
- pip install -r requirements.txt
- uvicorn app.main:app --reload

API Endpoints
- POST /shorten → Create short URL
- GET /{short_id} → Redirect to original URL
- Future Improvements
- Redis caching
- Rate limiting
- Analytics (click tracking)
- Custom short URLs

---

## 👉 Then commit:

``bash
git add README.md
git commit -m "added detailed README with project overview and setup instructions"
git push
