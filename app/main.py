from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not host or host.strip() == 'localhost':
        subprocess.call(['ping', host], shell=False)
    else:
        return {'error': 'Invalid or restricted host'}
    return {'status': 'completed'}