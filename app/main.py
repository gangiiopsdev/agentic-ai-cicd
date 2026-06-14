from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if host.isalnum():
        subprocess.call(['ping', host])
    else:
        raise ValueError('Invalid hostname')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}