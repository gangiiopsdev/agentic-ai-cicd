from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation using a whitelist of allowed hosts
    allowed_hosts = ['example.com', 'localhost']
    if host in allowed_hosts:
        subprocess.call(['ping', host])
    return {'status': 'completed'}