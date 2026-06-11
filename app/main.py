from fastapi import FastAPI
import subprocess
from pydantic import BaseModel, validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        if not all(c.isalnum() or c in ' .-' for c in v):
            raise ValueError('Invalid input')
        return v

@app.post("/ping")
def ping(request: PingRequest):
    host = subprocess.check_output(['echo', request.host]).decode().strip()
    try:
        result = subprocess.run(['ping', '-c 1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'response': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'response': f'Error: {e}'}