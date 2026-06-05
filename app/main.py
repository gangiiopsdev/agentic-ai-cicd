from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    if host == 'localhost' or host.startswith('127.0.0.1'):
        subprocess.call(['ping', host])
    else:
        raise ValueError('Ping to unknown hosts is not allowed.')

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}