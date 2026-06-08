from fastapi import FastAPI
import subprocess
import os

app = FastAPI()

def safe_ping(host: str):
    # Validate host input
    if not host.isalnum():
        raise ValueError('Invalid host name')
    # Use a full path for the command to mitigate issues with PATH manipulation attacks
    subprocess.run(['/sbin/ping', '-c', '1', host], check=True, shell=False)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if os.path.exists('/sbin/ping'):
        safe_ping(host)
    else:
        raise Exception('Ping executable not found')
    return {'status': 'completed'}