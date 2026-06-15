from fastapi import FastAPI
import subprocess
import os

def execute_ping(host):
    try:
        # Use os.path.join to ensure the full path of the executable is used
        result = subprocess.run([os.path.join('/usr/bin', 'ping'), host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

def validate_host(host):
    if not host.isalnum() or len(host) > 64:
        raise ValueError("Invalid host input")

app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    validate_host(host)
    result = execute_ping(host)
    return {'status': 'completed', 'result': result}