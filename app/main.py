from fastapi import FastAPI
import subprocess
def is_safe_host(host):
    safe_hosts = ['localhost', '127.0.0.1']
    return host in safe_hosts
class SafePing:
    def __call__(self, host: str):
        if not is_safe_host(host):
            raise ValueError('Unsafe host')
        subprocess.run(['ping', '-c 1', host], check=True, capture_output=True)

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    SafePing()(host)
    return {'status': 'completed'}