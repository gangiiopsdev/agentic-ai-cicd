from fastapi import FastAPI
import subprocess
from fastapi import HTTPException

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent injection attacks
    if not host.isalnum() or len(host) > 64:
        raise HTTPException(status_code=400, detail="Invalid host parameter")
    try:
        subprocess.call(["ping", host])
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e)}, 500