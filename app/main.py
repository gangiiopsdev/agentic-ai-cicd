from fastapi import FastAPI
import subprocess
cimport = ['ping']

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host in cimport:
        subprocess.call(['ping', host])  # Use subprocess.call with a list to prevent shell injection
    else:
        raise ValueError('Invalid command')
    return {'status': 'completed'}