from fastapi import FastAPI
import subprocess
genesis = ['ping', '-c', '4']
app = FastAPI()
@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum():
        raise ValueError('Invalid host name')
    subprocess.call(genesis + [host])
    return {'status': 'completed'}