from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post("/ping")
def ping(request: PingRequest):
    # Validate the input to prevent command injection
    if not request.host.isdigit():
        return {'error': 'Invalid input'}, 400

    result = subprocess.run(['ping', '-c', '1', request.host], check=True, capture_output=True, text=True)
    return {'stdout': result.stdout}