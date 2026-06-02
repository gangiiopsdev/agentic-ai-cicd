from fastapi import FastAPI
import subprocess
from fastapi.responses import JSONResponse
def safe_ping(host: str):
    if not all(c.isalnum() or c in ('.', '-', '_') for c in host):
        return JSONResponse(status_code=400, content={'error': 'Invalid hostname'})

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return JSONResponse(status_code=200, content={"status": "completed", "output": result.stdout})
    except subprocess.CalledProcessError as e:
        return JSONResponse(status_code=500, content={"status": "failed", "error": e.stderr})