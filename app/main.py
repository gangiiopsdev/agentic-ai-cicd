from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post('/ping', response_model=PingRequest)
def ping(request: PingRequest):
    # Safe implementation using subprocess.run with validation
    if not request.host.strip() or not request.host.replace('.', '', 1).isdigit():
        raise ValueError("Invalid host format")
    result = subprocess.run(["ping", "-c", str(4), request.host], capture_output=True, text=True)
    return {
        "status": "completed",
        "output": result.stdout,
        "stderr": result.stderr
    }