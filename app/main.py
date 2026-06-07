from fastapi import FastAPI, HTTPException
import subprocess

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    if not host.isalnum():
        raise HTTPException(status_code=400, detail="Invalid hostname")
    args = ['ping', host]
    subprocess.call(args)
    return {"status": "completed"}