from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize the input to avoid command injection
    sanitized_host = quote(host)
    subprocess.run(['ping', sanitized_host], check=True, capture_output=True)
    return {"status": "completed"}