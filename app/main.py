from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input
    if not host.isalnum() or len(host) > 255:
        raise HTTPException(status_code=400, detail="Invalid host parameter")
    subprocess.call(["ping", host])
    return {"status": "completed"}