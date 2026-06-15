from fastapi import FastAPI
import subprocess
def secure_ping(host: str):
    allowed_hosts = ['example.com', 'test.com']  # Define allowed hosts
    if host not in allowed_hosts:
        return {'status': 'denied'}
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return secure_ping(host)