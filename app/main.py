from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post("/ping")
def ping(request: PingRequest):
    host = request.host
    # Safe implementation with input validation and sanitization
    if not host.isalnum():
        raise ValueError("Invalid hostname")
    subprocess.call(["ping", subprocess.list2cmdline([host])])
    return {"status": "completed"}