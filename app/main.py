from fastapi import FastAPI, HTTPException
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.isnumeric() or len(host) != 3:
        raise HTTPException(status_code=400, detail="Invalid host format")
    subprocess.run(['ping', host], capture_output=True, text=True)
    return {"status": "completed"}