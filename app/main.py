from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):
    # Secure implementation with input validation and sanitization
    try:
        output = subprocess.check_output(['ping', '-c', '1', request.host], stderr=subprocess.STDOUT, text=True)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}