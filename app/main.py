from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    allowed_hosts = ['example.com', 'test.com']  # Define a list of allowed hosts
    if host in allowed_hosts:
        result = subprocess.run(shlex.split(f'ping -c 1 {host}'), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    else:
        return {'status': 'error', 'message': 'Host not allowed'}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)