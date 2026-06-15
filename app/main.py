from fastapi import FastAPI
import subprocess
def execute_safe_ping(host):
    # Safe implementation with input validation and sanitization
    if not host.strip().isdigit():
        raise ValueError('Invalid host input')
    subprocess.run(['ping', host], check=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    execute_safe_ping(host)
    return {'status': 'completed'}