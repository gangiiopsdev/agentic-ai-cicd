from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host.strip() == 'localhost':
        subprocess.call(['ping', host])
    else:
        return {'status': 'Invalid host'}
    return {'status': 'completed'}