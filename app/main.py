from fastapi import FastAPI
import subprocess
import shlex
from pydantic import validator

class SafePing:
    @staticmethod
    def ping(host: str):
        # Validate the host input
        if not all(c.isalnum() or c in '-.' for c in host):
            raise ValueError('Invalid host name')
        args = shlex.split(f'ping {host}')
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_endpoint(host: str):
    return SafePing.ping(host)