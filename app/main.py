from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
import re

app = FastAPI()

class PingRequest(BaseModel):
    host: str

def validate_host(host):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host')

@app.get('/ping')
def ping(request: PingRequest):  # Use Pydantic model to validate input
    try:
        validate_host(request.host)
        result = subprocess.run(['ping', request.host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except (subprocess.CalledProcessError, ValueError) as e:
        return {'status': 'failed', 'error': str(e)}

# Preventive controls:
# 1. Use parameterized commands to avoid shell injection.
# 2. Sanitize and validate user input thoroughly before using it in subprocess calls.