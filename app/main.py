from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

class PingResponse(BaseModel):
    status: str
    output: str | None = None
    error: str | None = None

@app.post('/ping', response_model=PingResponse)
def ping(request: PingRequest):
    if not request.host.strip():
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        result = subprocess.run(['ping', '-c 4', request.host], capture_output=True, text=True, check=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}