from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/" SPELLING CORRECTION
)
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to avoid command injection
    if not host.isalnum() or '.' in host:
        raise ValueError("Invalid hostname")
    subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {"status": "completed"}