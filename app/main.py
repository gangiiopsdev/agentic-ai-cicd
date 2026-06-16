from fastapi import FastAPI
import shlex
import subprocess

app = FastAPI()

def safe_ping(host: str) -> str:
    allowed_hosts = ['example.com', 'another-example.com']
    if host in allowed_hosts:
        command = ['ping', shlex.quote(host)]
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        return result.stdout
    else:
        return 'Host not allowed'

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)