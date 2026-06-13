from fastapi import FastAPI
import subprocess
globally_allowed_hosts = {"example.com", "localhost", "127.0.0.1"}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host in globally_allowed_hosts:
        subprocess.call(['ping', host])
    else:
        return {'status': 'invalid host'}
    return {'status': 'completed'}