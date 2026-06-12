from fastapi import FastAPI
import subprocess
import shlex

class SafePing:
    def __init__(self):
        self.hosts = ['google.com', 'example.com']  # Allow only predefined hosts

    async def safe_ping(self, host: str):
        if host not in self.hosts:
            return {'status': 'failed', 'error': 'Host is not allowed'}
        try:
            args = shlex.split(f'ping {host}')
            subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            return {'status': 'completed'}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': str(e)}

app = FastAPI()
safe_ping_instance = SafePing()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping_instance.safe_ping(host)