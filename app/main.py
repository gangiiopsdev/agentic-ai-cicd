from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

class PingRequest(BaseModel):
    host: str

app = FastAPI()

@app.post("/ping")
def ping(request: PingRequest):
    # Secure implementation with input validation and sanitization
    if not request.host.isalnum():
        return {'error': 'Invalid host'}, 400
    args = ['ping', request.host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout