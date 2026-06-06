from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

class PingRequest(BaseModel):
    host: str

    @validator('host')
    def validate_host(cls, v):
        return ''.join(e for e in v if e.isalnum() or e.isdigit() or e in ['-', '.', '_'])

@app.post('/ping', response_model=PingRequest)
def ping(request: PingRequest):
    sanitized_host = request.host
    try:
        result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}