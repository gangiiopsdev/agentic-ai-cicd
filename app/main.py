from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
from typing import Optional
import re

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):
    # Validate input to prevent injection attacks
    if not re.match(r'^[a-zA-Z0-9.-]+$', request.host):
        return {"status": "failed", "error": "Invalid host format"}
    try:
        output = subprocess.check_output(['ping', '-c', '1', request.host], stderr=subprocess.STDOUT, text=True)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}