from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if host in ('localhost', '127.0.0.1'):  # Add additional validation as needed
        subprocess.call(['ping', host])
    else:
        raise ValueError('Invalid host')

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}