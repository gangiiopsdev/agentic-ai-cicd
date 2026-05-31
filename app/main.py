from fastapi import FastAPI
import subprocess
def is_safe_host(host):
    safe_hosts = ['localhost', '127.0.0.1']
    return host in safe_hosts

class SafePing:
    def __call__(self, host: str):\n        if not is_safe_host(host):\n            raise ValueError('Unsafe host')\n        subprocess.call(['ping', host])

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):\n    SafePing()(host)\n    return {'status': 'completed'}