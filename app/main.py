from fastapi import FastAPI
import subprocess

app = FastAPI()

allowed_hosts = ['8.8.8.8', '127.0.0.1']

def safe_ping(host: str):
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')
    subprocess.call(['ping', '-c', '4', host], shell=False)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}