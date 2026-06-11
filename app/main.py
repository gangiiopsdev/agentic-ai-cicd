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

@app.post('/ping')
def ping(request: PingRequest):
    try:
        subprocess.run(generate_ping_command(request.host), shell=False, check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}