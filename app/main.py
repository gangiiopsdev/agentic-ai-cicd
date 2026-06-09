from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    if not host.isalnum():
        raise ValueError("Invalid host")
    subprocess.call(['ping', host])

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        safe_ping(host)
        return {'status': 'completed'}
    except ValueError as e:
        return {'error': str(e)}