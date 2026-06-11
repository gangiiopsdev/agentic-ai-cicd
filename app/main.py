from fastapi import FastAPI
import subprocess
from fastapi import HTTPException

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input
    if not host.isalnum():
        raise HTTPException(status_code=400, detail="Invalid host name")
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {"status": result.stdout.strip()}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}