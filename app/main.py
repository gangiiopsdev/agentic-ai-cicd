from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

def safe_ping(host: str):
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    return {'status': 'completed', 'output': result.stdout, 'returncode': result.returncode}

@app.post("/ping")
def ping(request: PingRequest):
    # Validate and sanitize input here if necessary
    result = safe_ping('127.0.0.1')  # Example hardcoded host
    return result