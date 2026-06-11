from fastapi import FastAPI, HTTPException
import subprocess
import re

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Input validation for host
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise HTTPException(status_code=400, detail="Invalid host format")
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {"status": "completed"}

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}