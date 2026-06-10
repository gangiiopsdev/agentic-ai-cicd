from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
class PingRequest(BaseModel):
    host: str

app = FastAPI()

@app.post('/ping')
def ping(request: PingRequest):
    # Secure implementation
    if not request.host.startswith('192.168.'):  # Example of a simple validation rule
        return {'status': 'error', 'message': 'Invalid host'}
    args = ['ping', request.host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}