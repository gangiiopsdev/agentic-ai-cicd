from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self, allowed_hosts):
        self.allowed_hosts = set(allowed_hosts)

    async def ping(self, host: str):
        if host not in self.allowed_hosts:
            raise ValueError(f'Host {host} is not allowed')
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}

app = FastAPI()
safe_ping = SafePing(allowed_hosts=['example.com'])

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        return await safe_ping.ping(host)
    except ValueError as e:
        return {'status': 'failed', 'error': str(e)}