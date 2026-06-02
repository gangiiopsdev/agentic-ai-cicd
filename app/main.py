from fastapi import FastAPI
import subprocess

app = FastAPI()

def secure_ping(host: str):
    if 'ping' in host or '&' in host:
        return {'status': 'invalid request'}
    args = ['ping', host]
    subprocess.call(args)
    return {'status': 'completed'}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return secure_ping(host)