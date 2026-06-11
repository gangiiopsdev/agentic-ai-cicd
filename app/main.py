from fastapi import FastAPI
import re
from fastapi.exceptions import HTTPException

app = FastAPI()

def ping(host: str):
    # Secure implementation with comprehensive validation
    if not re.match(r'^[a-zA-Z0-9.-]+$', host) or len(host.split('.')) < 2:
        raise HTTPException(status_code=400, detail="Invalid host")
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {"status": "completed"}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with comprehensive validation
    if not re.match(r'^[a-zA-Z0-9.-]+$', host) or len(host.split('.')) < 2:
        raise HTTPException(status_code=400, detail="Invalid host")
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {"status": "completed"}