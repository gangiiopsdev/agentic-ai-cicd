from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
from typing import Optional
import shlex

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post('/ping')
def ping(request: PingRequest):
    args = ['ping', request.host]  # Avoid using shlex.quote for command arguments
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}