from fastapi import FastAPI
import subprocess
cimport = { 'ping': 'ping' }

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host not in cimport:
        return {'error': 'Invalid host'}, 400
    subprocess.call([cimport[host], host])
    return {'status': 'completed'}