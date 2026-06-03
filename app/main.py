from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def ping(host: str):
        args = shlex.split(f'ping {host}')
        subprocess.run(args, check=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate the host input
    if not host.isalnum() and '.' not in host:
        raise ValueError('Invalid host format')
    sanitized_host = ''.join(c for c in host if c.isalnum() or c == '.')  # Sanitize host input
    SafeSubprocess.ping(shlex.quote(sanitized_host))
    return {'status': 'completed'}