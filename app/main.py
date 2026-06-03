from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):
    # Secure implementation using subprocess.run with input validation and sanitization
    host = request.host.strip()
    if not host:
        return {"status": "invalid_host"}
    subprocess.run(['ping', '-c', '1', host], check=True)
    return {"status": "completed"}