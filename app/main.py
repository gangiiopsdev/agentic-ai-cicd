from fastapi import FastAPI
import subprocess
from typing import List
from pydantic import BaseModel
class PingRequest(BaseModel):
    host: str
app = FastAPI()
@app.post("/ping")
def ping(request: PingRequest):
    # Secure implementation
    try:
        subprocess.run(['ping', request.host], check=True, shell=False)
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}
    return {"status": "completed"}