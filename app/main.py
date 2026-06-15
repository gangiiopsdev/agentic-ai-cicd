from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not host.startswith('192.168.') and not host.startswith('172.16.'):
        return {'status': 'invalid host'}
    safe_host = subprocess.list2cmdline([host])  # Sanitize the input to avoid shell injection
    subprocess.run(['ping', safe_host], check=True, shell=False)
    return {'status': 'completed'}