from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):
    try:
        # Validate the input to ensure it does not contain any malicious characters
        if '\' in request.host or '"' in request.host:
            return {'status': 'failed', 'error': 'Invalid host'}
        result = subprocess.run(['ping', '--'] + request.host.split('\s'), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}