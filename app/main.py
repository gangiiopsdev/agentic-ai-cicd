from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/"`

def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
async def ping(host: str):
    # Validate input to prevent injection attacks
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {"status": "failed", "result": "Invalid input"}
    try:
        subprocess.run(['ping', '-c', '1', host], check=True, timeout=5)
        return {"status": "completed", "result": "Success"}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "result": str(e)}