from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator
import re
def is_valid_host(value):
    if not re.match(r'^[a-zA-Z0-9.-]+$', value):
        raise ValueError('Invalid hostname')

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):
    args = ['ping', request.host]
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return {"status": "completed", "output": result.stdout}