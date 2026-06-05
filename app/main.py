from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

allowed_hosts = ['example.com', 'test.com']

async def ping(host: str):
    if host not in allowed_hosts:
        return {'status': 'error', 'message': 'Host not allowed'}
    # Secure implementation with shell=True for proper handling of command arguments
    cmd = shlex.split('ping ' + host)
    result = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}

@app.get("/")
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get("/ping")
def ping_secure(host: str):
    # Secure implementation with input validation and sanitization
    if host not in allowed_hosts:
        return {'status': 'error', 'message': 'Host not allowed'}
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}