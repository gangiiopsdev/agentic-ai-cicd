from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self, allowed_hosts=None):
        self.allowed_hosts = allowed_hosts or []

    def ping(self, host: str):
        if host in self.allowed_hosts:
            subprocess.call(['ping', host])

app = FastAPI()
safe_ping = SafePing(allowed_hosts=['example.com'])

def ping_endpoint(host: str):
    return safe_ping.ping(host)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}