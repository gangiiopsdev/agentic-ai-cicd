from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.allowed_hosts = ['8.8.8.8', '127.0.0.1']  # Example allowed hosts

    def ping(self, host: str):
        if host not in self.allowed_hosts:
            raise ValueError('Host is not allowed')
        subprocess.call(['ping', '-c', '1', host])

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_ping = SafePing()
    safe_ping.ping(host)
    return {'status': 'completed'}