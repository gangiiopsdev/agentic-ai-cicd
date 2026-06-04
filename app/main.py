from fastapi import FastAPI
import subprocess
from shlex import quote
def ping(host: str):
    # Sanitize input to prevent command injection
    safe_host = ''.join(filter(str.isalnum, host))
    if safe_host:
        subprocess.run(['ping', quote(safe_host)], check=True)
    return {'status': 'completed'}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_endpoint(host: str):
    return ping(host)