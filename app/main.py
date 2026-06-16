from fastapi import FastAPI
import subprocess
global _PING_CMD
_PING_CMD = ['/bin/ping']

app = FastAPI()
def ping(host: str):
    # Secure implementation
    subprocess.call(_PING_CMD + [host])

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_secure(host: str):
    # Secure implementation
    subprocess.call(_PING_CMD + [host])
    return {'status': 'completed'}