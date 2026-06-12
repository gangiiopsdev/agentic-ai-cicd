from fastapi import FastAPI
import subprocess
globally_whitelisted_hosts = ['example.com', 'localhost']

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host in globally_whitelisted_hosts:
        subprocess.call(['ping', host])
    else:
        raise ValueError('Invalid host')
    return {'status': 'completed'}