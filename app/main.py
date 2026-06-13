from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host):
    allowed_hosts = ['example.com', 'localhost']  # List of allowed hosts
    return host in allowed_hosts

class PingService:
    def __init__(self, allowed_hosts):
        self.allowed_hosts = allowed_hosts

    async def ping(self, host):
        if not validate_host(host):
            raise ValueError('Invalid host')
        args = shlex.split(f'ping {host}')
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'result': result.stdout}

app = FastAPI()
ping_service = PingService(allowed_hosts=['example.com', 'localhost'])

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return ping_service.ping(host)