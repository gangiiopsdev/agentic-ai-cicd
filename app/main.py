from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

class PingResponse(BaseModel):
    status: str
    output: str
    error: Optional[str] = None

@app.post("/ping", response_model=PingResponse)
def ping(request: PingRequest):
    try:
        result = subprocess.run(['ping', request.host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
        return {'status': 'completed', 'output': result.stdout.decode(), 'error': None}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'output': None, 'error': e.stderr.decode()}