from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
def safe_ping(host: str) -> bool:
    allowed_hosts = ['example.com', 'another-example.com']  # Replace with actual allowed hosts
    return host in allowed_hosts

app = FastAPI()

class PingRequest(BaseModel):
    host: str

def execute_command(command: list[str]) -> dict:
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

@app.post('/ping')
def ping(request: PingRequest):
    if not safe_ping(request.host):
        return {'status': 'error', 'message': 'Invalid host'}
    command = ['ping', request.host]
    return execute_command(command)