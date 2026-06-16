from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
import re

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):
    # Validate the input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', request.host):
        return {"status": "failed", "error": "Invalid host name"}
    args = ['ping', request.host]
    try:
        subprocess.run(args, check=True)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}