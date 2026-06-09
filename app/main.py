from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
import os

app = FastAPI()

class PingRequest(BaseModel):
    host: str

@app.post('/ping')
def ping(request: PingRequest):
    # Secure implementation
    try:
        if request.host == 'localhost' or request.host.endswith('127.0.0.1'):  # Example of basic validation
            command = ['ping', request.host]
            output = subprocess.run(command, capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': output.stdout}
        else:
            return {'status': 'failed', 'error': 'Invalid host'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}