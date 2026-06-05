from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
def generate_ping_command(host: str) -> str:
    return f'ping {host}'

class PingRequest(BaseModel):
    host: str

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.post('/ping', response_model=dict)
def ping(request: PingRequest):
    # Validate the input to prevent injection attacks
    if not request.host.isnumeric():
        return {'status': 'error', 'message': 'Invalid host'}
    command = generate_ping_command(request.host)
    result = subprocess.run(command.split(), capture_output=True, text=True)
    return {'status': 'completed', 'stdout': result.stdout}