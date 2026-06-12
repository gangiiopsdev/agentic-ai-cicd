from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host in ['127.0.0.1', '::1']:  # Allow only local hosts for safety
        subprocess.call(['ping', subprocess.list2cmdline([host])])
    else:
        return {'error': 'Invalid host'}
    
    return {'status': 'completed'}