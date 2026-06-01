from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    @staticmethod
def safe_ping(host: str):
        if not host.isalnum() or '-' not in host:
            raise ValueError('Invalid host name')
        cmd = ['ping', *shlex.split(host)]
        subprocess.call(cmd)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        SafePing.safe_ping(host)
        return {'status': 'completed'}
    except ValueError as e:
        return {'error': str(e)}