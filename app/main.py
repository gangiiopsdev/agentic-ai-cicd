from fastapi import FastAPI
import subprocess
from fastapi import HTTPException

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        raise HTTPException(status_code=400, detail="Invalid hostname")
    # Secure implementation
    subprocess.call(["ping", host])
    return {"status": "completed"}