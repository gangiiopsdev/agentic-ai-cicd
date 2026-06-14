from fastapi import FastAPI
import subprocess
from shlex import quote
def safe_ping(host: str) -> bool:
    try:
        host = quote(host, safe='')
        result = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True)
        return True
    except subprocess.CalledProcessError as e:
        print(e.stderr.decode())
        return False

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if safe_ping(host):
        return {'status': 'completed'}
    else:
        return {'status': 'failed', 'reason': 'Invalid host'}, 400