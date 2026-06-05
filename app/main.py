from fastapi import FastAPI
import subprocess
import shlex
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post('/ping')
def ping(request: PingRequest):
    sanitized_host = shlex.quote(request.host)  # Use shlex.quote to safely escape user input
    command = ['ping', sanitized_host]  # Avoid using subprocess.run directly to prevent shell injection
    try:
        subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}