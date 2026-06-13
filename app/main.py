from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):
    # Secure implementation with input validation and sanitization
    if not request.host.isdigit():
        return {"status": "error", "message": "Invalid host format"}
    subprocess.call(['ping', request.host])
    return {"status": "completed"}