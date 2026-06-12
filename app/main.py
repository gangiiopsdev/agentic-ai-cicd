from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if host.strip().isnumeric() and 0 <= int(host) <= 255:
        subprocess.call(['ping', '-c', '1', host])
    else:
        return {'status': 'error', 'message': 'Invalid host'}
    return {'status': 'completed'}