from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

def safe_ping(host):
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.post("/ping")
def ping(request: PingRequest):
    # Validate input to prevent command injection
    if not request.host.isalnum():
        raise ValueError("Invalid input for ping")
    response = safe_ping(request.host)
    return {'status': 'completed', 'response': response}