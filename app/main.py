from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def safe_ping(host):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not os.path.exists('/sbin/ping'):  # Check if 'ping' exists in the system path
        return {'status': 'failed', 'error': 'Ping command not available'}
    return safe_ping(host)