from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.allowed_hosts = ['example.com', 'test.example.com']

    def ping(self, host: str):
        if host in self.allowed_hosts:
            args = ['ping', host]
            subprocess.call(args)
            return {'status': 'completed'}
        else:
            raise ValueError('Host is not allowed')

app = FastAPI()
safe_ping = SafePing()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping.ping(host)