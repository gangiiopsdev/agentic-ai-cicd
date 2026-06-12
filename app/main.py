from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):
    # Secure implementation
    if request.host and isinstance(request.host, str) and all(c.isalnum() or c in ['-', '.', '_', '!'] for c in request.host):
        subprocess.call(["ping", request.host], shell=False)
        return {"status": "completed"}
    else:
        return {"error": "Invalid host name"}