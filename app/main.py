from fastapi import FastAPI
import subprocess
from pydantic import BaseModel

class PingRequest(BaseModel):
    host: str

def validate_host(host):
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts

app = FastAPI()

@app.get('/', response_model=dict)
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.post('/ping', response_model=dict)
def ping(request: PingRequest):
    if validate_host(request.host):
        try:
            output = subprocess.run(['ping', request.host], capture_output=True, text=True, check=True)
            return {'status': 'completed', 'output': output.stdout}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.stderr}
    else:
        return {'status': 'failed', 'error': 'Invalid host'}

# Add additional security measures to mitigate the risk of arbitrary code execution.
# For example, use a whitelist of allowed hosts and validate input more rigorously.