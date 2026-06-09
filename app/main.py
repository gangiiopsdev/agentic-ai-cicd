from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run with absolute path for 'ping'
    result = subprocess.run(['/usr/bin/ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_safe(host: str):
    return ping(host)