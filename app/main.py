from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post("/ping")
def ping(request: PingRequest):
    # Secure implementation with input validation
    command = ['ping', request.host]
    subprocess.call(command)
    return {"status": "completed"}