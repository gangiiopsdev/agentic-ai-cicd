from fastapi import FastAPI, HTTPException
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input
    if not host.replace('.', '').isdigit() or len(host.split('.')) != 4:
        raise HTTPException(status_code=400, detail="Invalid IP address format")
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}