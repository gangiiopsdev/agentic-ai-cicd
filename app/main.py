from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['127.0.0.1', 'localhost']
    if host in allowed_hosts:
        return True
    else:
        raise ValueError("Invalid host")

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if validate_host(host):
        subprocess.run(['ping', host], check=True)
        return {'status': 'completed'}