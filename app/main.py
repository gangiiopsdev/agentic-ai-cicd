from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    if not host or len(host) > 255 or not all(c.isalnum() or c in '.-_' for c in host):
        raise ValueError("Invalid host name")

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    validate_host(host)
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}