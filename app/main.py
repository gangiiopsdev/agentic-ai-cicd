from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post("/ping")
def ping(request: PingRequest):
    # Validate the input to prevent command injection
    if request.host.isalnum() and '.' in request.host:
        command = ['ping', request.host]
        subprocess.call(command)
    else:
        return {"status": "error", "message": "Invalid host"}
    return {"status": "completed"}