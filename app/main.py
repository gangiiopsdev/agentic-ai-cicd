from fastapi import FastAPI
import subprocess
from pydantic import validator

class PingRequest:
    host: str

    @validator('host')
    def validate_host(cls, v):
        return v.replace('.', '').replace('-', '').isalnum()

app = FastAPI()

@app.post('/ping')
def ping(request: PingRequest):
    command = ['ping', request.host]
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}