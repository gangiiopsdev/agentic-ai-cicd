from fastapi import FastAPI
import subprocess
def safe_ping(host):
    if host in allowed_hosts:
        command = ['ping', host]
        subprocess.call(command)

app = FastAPI()

allowed_hosts = {'127.0.0.1', 'localhost'}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if safe_ping(host):
        return {'status': 'completed'}