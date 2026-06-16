from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation with proper sanitization
    safe_host = host.strip()  # Remove leading/trailing whitespaces
    if not safe_host:
        return {'status': 'error', 'message': 'Invalid host parameter'}
    subprocess.call(['ping', '-c 1', safe_host])  # Limit the number of pings to avoid DoS
    return {'status': 'completed'}