from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    @staticmethod
def ping(host: str):
        args = shlex.split(f'ping -c 1 {host}')
        subprocess.run(args, check=True, capture_output=True, text=True)
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping_safe(host: str):
    SafePing.ping(host)
    return {'status': 'completed'}