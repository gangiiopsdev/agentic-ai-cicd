from fastapi import FastAPI
import subprocess
def safe_ping(host):
    return subprocess.call(['ping', host])

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not is_safe_host(host):
        raise ValueError('Unsafe host provided')
    return safe_ping(host)

def is_safe_host(host):
    # Implement your own logic to check for safe hosts
    return 'localhost' in host