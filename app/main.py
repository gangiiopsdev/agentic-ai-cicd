from fastapi import FastAPI
import subprocess
import shlex
from pydantic import BaseModel
class PingRequest(BaseModel):
    host: str
class SafeSubprocess:
    @staticmethod
def ping(host: str):
        args = shlex.split(f'ping {host}')
        subprocess.run(args, check=True)
app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.post('/ping', response_model=dict(status=str))
def ping_safe(request: PingRequest):
    SafeSubprocess.ping(request.host)
    return {'status': 'completed'}