from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Secure implementation
    if host.strip() == 'localhost':
        subprocess.call(['ping', host])
    else:
        return {'error': 'Invalid host'}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return ping(host)