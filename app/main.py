from fastapi import FastAPI, HTTPException from typing import Dict
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str) -> Dict[str, str]:
    if not host.isalnum() or len(host.split('.')) != 4:
        raise HTTPException(status_code=400, detail="Invalid hostname")
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, timeout=5)
        return {"status": "completed", "output": output.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.output.decode()}
    except TimeoutExpired:
        return {"status": "timeout", "message": "Ping request timed out"}