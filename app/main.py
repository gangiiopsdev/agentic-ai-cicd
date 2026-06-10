from fastapi import FastAPI
import subprocess
import shlex
from pydantic import BaseModel

app = FastAPI()

class PingRequest(BaseModel):
    host: str

allowed_hosts = ['127.0.0.1', '::1']  # Example allowed hosts

def ping(request: PingRequest):
    if request.host not in allowed_hosts:
        return {'error': 'Host not allowed'}, 403
    command = shlex.split(f'ping -c 1 {shlex.quote(request.host)}')
    try:
        subprocess.run(command, check=True, text=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': f'Ping failed: {e}'}, 500

@app.get("/")
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.post(
    "/ping",
    response_model=BaseModel,
)
def ping_post(request: PingRequest):
    return ping(request)