from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get('/ping')
def ping(request: PingRequest):
    # Sanitize user input
    if not request.host.isalnum() or len(request.host) > 64:
        return {'status': 'failed', 'error': 'Invalid host name'}
    try:
        output = subprocess.run(['ping', '-c', '1', '--', request.host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}