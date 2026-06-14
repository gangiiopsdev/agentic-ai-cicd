from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.get("/ping")
def ping(request: PingRequest):
    try:
        # Validate and sanitize the input to prevent command injection
        if not request.host.strip().replace('.', '').isalnum():
            return {'status': 'failed', 'error': 'Invalid host'}
        output = subprocess.run(['ping', f'-c 1 {request.host}'], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}