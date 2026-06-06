from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post('/ping', response_model=dict)
async def ping(request: PingRequest):
    # Sanitize user input to avoid command injection
    if '&&' in request.host or ';' in request.host or '|' in request.host:
        return {'status': 'error', 'message': 'Invalid input'}
    args = ['ping', request.host]
    result = subprocess.run(args, check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}