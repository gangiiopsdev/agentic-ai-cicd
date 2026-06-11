from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):,
    host = request.host
    # Secure implementation
    try:
        subprocess.call(["ping", host], shell=False)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e)}, 500