from fastapi import FastAPI
import subprocess
from typing import Optional
from pydantic import BaseModel
global ping_lock
ping_lock = threading.Lock()

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):
    global ping_lock
    with ping_lock:
        try:
            result = subprocess.run(['ping', request.host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
            return {"status": "completed", "output": result.stdout.decode()}
        except subprocess.CalledProcessError as e:
            return {"status": "error", "error": str(e)}