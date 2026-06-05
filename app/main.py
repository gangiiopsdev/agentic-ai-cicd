from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
import shlex

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post("/ping")
def ping(request: PingRequest):
    # Secure implementation using shlex.quote to prevent injection attacks
    command = ['ping', shlex.quote(request.host)]
    subprocess.call(command)
    return {"status": "completed"}