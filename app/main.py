from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host in ['127.0.0.1', '::1']:  # Allow only local pinging for security reasons
        subprocess.call(['ping', '-c', '4', host], shell=False)
    else:
        return {'status': 'error', 'message': 'Invalid host'}
    return {'status': 'completed'}