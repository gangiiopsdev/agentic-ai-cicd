from fastapi import FastAPI
import subprocess
import shlex
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post("/ping")
def ping(request: PingRequest):
    args = shlex.split(f'ping {shlex.quote(request.host)}')
    subprocess.call(args)
    return {"status": "completed"}