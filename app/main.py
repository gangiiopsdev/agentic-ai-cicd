from fastapi import FastAPI
import subprocess
from fastapi.exceptions import HTTPException

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation with validation and sanitization
    allowed_hosts = ["example.com", "test.com"]  # Define a list of allowed hosts
    if host not in allowed_hosts:
        raise HTTPException(status_code=403, detail="Unauthorized host")
    subprocess.call(["ping", host])
    return {"status": "completed"}