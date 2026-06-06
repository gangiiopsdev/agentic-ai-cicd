from fastapi import FastAPI
import subprocess
def is_valid_host(host):
    parts = host.split('.')
    return len(parts) == 2 and all(part.isalnum() for part in parts)
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    if is_valid_host(host):
        subprocess.call(['ping', host], shell=False)
    else:
        return {'status': 'invalid input'}
    return {'status': 'completed'}