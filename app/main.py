from fastapi import FastAPI
import subprocess
import shlex

class SafePing:
    def __init__(self):
        self.allowed_hosts = ['127.0.0.1', '::1']

    async def safe_ping(self, host: str):
        if host not in self.allowed_hosts:
            raise ValueError('Invalid host')
        args = shlex.split(f'ping {host}')
        subprocess.run(args, check=True)

app = FastAPI()
safe_ping_instance = SafePing()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_ping_instance.safe_ping(host)
    return {'status': 'completed'}