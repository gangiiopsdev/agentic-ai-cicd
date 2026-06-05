from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Safe implementation
    args = ['ping', host]
    subprocess.run(args, check=True)

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent injection attacks
    if not host.isalnum():
        raise ValueError('Invalid host name')
    safe_ping(host)
    return {'status': 'completed'}