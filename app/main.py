from fastapi import FastAPI
import subprocess
from fastapi import HTTPException

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize user input to prevent command injection
    if not host.isalnum() or ' ' in host:
        raise HTTPException(status_code=400, detail="Invalid hostname")
    subprocess.call(["ping", host])
    return {"status": "completed"}