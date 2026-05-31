from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post('/ping', response_model=BaseModel)
def ping(request: PingRequest):
    if not request.host.isdigit():
        return {'status': 'error', 'message': 'Invalid host input'}
    result = subprocess.run(['ping', '-c', '1', request.host], capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}

# Add exception handling and logging to improve security