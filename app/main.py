from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
from shlex import quote

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post('/ping')
def ping(request: PingRequest):
    # Validate the input to ensure it is a valid hostname or IP address
    if not re.match(r'^[a-zA-Z0-9.-]+$', request.host):
        return {'status': 'failed', 'error': 'Invalid host provided'}

    try:
        result = subprocess.run(['ping', quote(request.host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}