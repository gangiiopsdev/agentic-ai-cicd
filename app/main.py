from fastapi import FastAPI
import asyncio
import shlex
import subprocess
def safe_ping(host: str):
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid input'}
    # Use a whitelist of allowed hosts or IP ranges
    allowed_hosts = ['example.com', '192.168.1.1']
    if host not in allowed_hosts:
        return {'status': 'error', 'message': 'Host not allowed'}
    command = ['ping'] + shlex.split(host)
    try:
        result = await asyncio.subprocess.run(command, capture_output=True, text=True, check=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)