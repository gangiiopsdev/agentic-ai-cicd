from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate the host input to prevent command injection
    if not all(c.isalnum() or c in '._-' for c in host) or not host.startswith('192.168.'): raise ValueError("Invalid host name")

    # Secure implementation using subprocess.run with shell=False
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}