from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def ping(host: str):
    # Sanitize input to prevent command injection
    safe_host = ''.join(filter(str.isalnum, host))
    if safe_host:
        subprocess.call(['ping', quote(safe_host)])
    return {'status': 'completed'}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_endpoint(host: str):
    return ping(host)