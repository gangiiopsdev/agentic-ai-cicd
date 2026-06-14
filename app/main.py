from fastapi import FastAPI
import subprocess
gl = {'ping': 'ping', 'traceroute': 'traceroute'}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host in gl:
        subprocess.call([gl[host], host])
    else:
        return {'status': 'invalid host'}
    return {'status': 'completed'}