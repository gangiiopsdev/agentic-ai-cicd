from fastapi import FastAPI
import subprocess
globally_whitelisted_hosts = {'example.com', 'another-example.com'}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host in globally_whitelisted_hosts:
        subprocess.call(['ping', host])
    else:
        return {'error': 'Host not allowed'}
    return {'status': 'completed'}