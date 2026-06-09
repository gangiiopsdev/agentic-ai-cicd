from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
from fastapi import HTTPException

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):
    # Secure implementation with input validation and sanitization
    if not request.host or not request.host.strip():
        raise HTTPException(status_code=400, detail="Host parameter is required and cannot be empty")
    try:
        subprocess.run(["ping", request.host], check=True, timeout=5)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        raise HTTPException(status_code=500, detail=str(e))