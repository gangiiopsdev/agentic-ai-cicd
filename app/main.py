from fastapi import FastAPI
import subprocess
import shlex
from pydantic import BaseModel

class PingRequest(BaseModel):
    host: str

app = FastAPI()

@app.post('/ping')
def ping(request: PingRequest):
    # Validate and sanitize the input
    if not request.host or len(request.host) > 255:
        raise ValueError('Invalid host parameter')
    args = ['ping', '-c', '1', shlex.quote(request.host)]
    try:
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': e.stderr}