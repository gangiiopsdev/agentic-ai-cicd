from fastapi import FastAPI
import subprocess
def safe_ping(host):
    allowed_hosts = ['example.com']  # List of allowed hosts
    if host in allowed_hosts:
        subprocess.call(['ping', host], shell=False)
    else:
        raise ValueError('Host not allowed')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}