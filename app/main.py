from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.allowed_hosts = ['127.0.0.1', '::1']

    def ping(self, host: str):
        if host in self.allowed_hosts:
            return subprocess.call(['ping', '-c', '4', host])
        else:
            raise ValueError('Invalid host')

app = FastAPI()
safe_ping = SafePing()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping.ping(host)