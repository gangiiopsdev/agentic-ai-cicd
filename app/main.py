from fastapi import FastAPI
import subprocess
import shlex
class PingService:
    @staticmethod
def safe_ping(host: str) -> dict:
        if not host or len(host) > 255:
            return {'status': 'failed', 'error': 'Invalid host'}
        try:
            args = shlex.split(f'ping {host}')
            subprocess.run(args, check=True)
            return {'status': 'completed'}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return PingService.safe_ping(host)