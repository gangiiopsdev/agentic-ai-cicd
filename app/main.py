from fastapi import FastAPI
import subprocess
from pydantic import BaseModel
generate_ping_command = lambda host: f'ping {host}'

class PingRequest(BaseModel):
    host: str

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.post('/ping', response_model=dict)
def ping(request: PingRequest):
    command = generate_ping_command(request.host)
    result = subprocess.run(command, shell=False, capture_output=True, text=True)
    return {'status': 'completed', 'stdout': result.stdout}