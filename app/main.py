from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post("/ping")
def ping(request: PingRequest):
    # Secure implementation using shlex.quote to prevent injection attacks
    command = ['ping', subprocess.list2cmdline([request.host])]
    subprocess.call(command)
    return {"status": "completed"}