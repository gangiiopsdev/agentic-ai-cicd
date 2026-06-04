from fastapi import FastAPI
import subprocess
import shlex
class PingService:
    @staticmethod
def ping(host: str):
        safe_host = shlex.quote(host)
        args = ['ping', safe_host]
        subprocess.run(args, check=True, capture_output=True, text=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_host(host: str):
    if not host.isalnum() and not '.' in host:
        return {'error': 'Invalid input'}, 400
    PingService.ping(host)
    return {'status': 'completed'}