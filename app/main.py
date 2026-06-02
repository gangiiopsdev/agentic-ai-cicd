from fastapi import FastAPI
import subprocess
generics = ['192.168.0.1', '8.8.8.8'] # Allowed hosts list

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host in generics:
        subprocess.call(['ping', host])
    else:
        return {'status': 'Invalid host'}
    return {'status': 'completed'}