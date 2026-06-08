from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

def ping_endpoint(request: PingRequest):
    # Validate the input to ensure it does not contain malicious characters
    if any(char in request.host for char in [';', '|', '&', '&&', '||', '`', '\']):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        output = subprocess.run(['ping', '-c 4', request.host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}