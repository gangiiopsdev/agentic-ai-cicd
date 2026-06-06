from fastapi import FastAPI
import subprocess
global_pinger = ['ping', 'google.com']

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host in global_pinger:
        subprocess.call(global_pinger)
    else:
        return {'error': 'Host not allowed'}
    return {'status': 'completed'}