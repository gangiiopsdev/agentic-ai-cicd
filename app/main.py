from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):
    # Validate input to prevent command injection
    if not request.host.strip() or any(c in request.host for c in [';', '&', '|', '$', '`']):
        return {'error': 'Invalid input'}, 400
    result = subprocess.run(['ping', request.host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}