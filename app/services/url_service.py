import string
import random

url_db = {}

def generate_id(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def shorten_url(long_url):
    while True:
        short_id = generate_id()
        if short_id not in url_db:
            break

    url_db[short_id] = long_url
    return f"http://localhost:8000/{short_id}"

def get_original_url(short_id):
    return url_db.get(short_id)