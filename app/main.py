from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Ensure that only allowed hosts can be pinged
    if host not in ['example.com', 'another.example.com']:
        return {'status': 'error', 'message': 'Invalid host'}

    # Fixed implementation
    subprocess.call(['ping', host])
    return {'status': 'completed'}

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/safe-ping')
def ping(host: str):
    return safe_ping(host)