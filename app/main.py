from fastapi import FastAPI
import subprocess
from fastapi.responses import JSONResponse
def safe_ping(host: str) -> bool:
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, timeout=5)
        if result.returncode == 0:
            return True
        else:
            return False
    except subprocess.TimeoutExpired:
        return False

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        return JSONResponse(content={"status": "completed"}, status_code=200)
    else:
        return JSONResponse(content={"error": "Ping failed"}, status_code=500)