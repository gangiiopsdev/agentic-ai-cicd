from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Safe implementation using list for command parameters and validation
    if not host.isalnum():
        raise ValueError('Invalid host name')
    args = ['ping', host]
    subprocess.run(args)

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}