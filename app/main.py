from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
from typing import List

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):
    host = request.host.strip()
    if not host or any(c in host for c in (';', '&', '|', '<', '>', '`')):
        return {"status": "error", "result": "Invalid input"}
    command = ['ping', host]
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    return {"status": "completed", "result": result.stdout}