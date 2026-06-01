from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post('/ping', response_model=BaseModel)
def ping(request: PingRequest):
    if not request.host.isdigit():
        return {'status': 'error', 'message': 'Invalid host input'}
    try:
        result = subprocess.run(['ping', '-c', '1', request.host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}
    except Exception as e:
        return {'status': 'error', 'message': 'An unexpected error occurred'}