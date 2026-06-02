from fastapi import FastAPI
import subprocess
import shlex
def ping(host: str):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, shell=False)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_host(host: str):
    # Validate and sanitize input for 'host'
    if not host or len(host) > 255:
        return {'status': 'failed', 'error': 'Invalid host'}
    # Use shlex to safely handle shell arguments
    safe_host = shlex.quote(host)
    try:
        output = subprocess.check_output(['ping', safe_host], stderr=subprocess.STDOUT, shell=False)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}