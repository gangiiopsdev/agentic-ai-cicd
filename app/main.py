from fastapi import FastAPI
import subprocess
from urllib.parse import urlparse

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the input to prevent command injection
    try:
        result = urlparse(host)
        if not all(c.isalnum() or c in ('.', '-', '_') for c in result.netloc):
            raise ValueError("Invalid hostname")
    except ValueError as e:
        raise ValueError(e)
    subprocess.call(["ping", result.netloc])
    return {"status": "completed"}