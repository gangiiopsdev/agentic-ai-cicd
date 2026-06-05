from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self, safe_hosts):
        self.safe_hosts = safe_hosts

    async def ping(self, host: str):
        if host in self.safe_hosts:
            subprocess.call(['ping', host])

app = FastAPI()
safe_ping_service = SafePing(safe_hosts=['example.com'])

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping_service.ping(host)