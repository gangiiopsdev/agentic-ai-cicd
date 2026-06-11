from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
import re

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):
    # Secure implementation
    if not re.match(r'^[a-zA-Z0-9.-]+$', request.host):
        return {"status": "error", "message": "Invalid hostname"}
    subprocess.run(['ping', request.host], check=True)
    return {"status": "completed"}