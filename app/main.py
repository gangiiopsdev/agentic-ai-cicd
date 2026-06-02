from fastapi import FastAPI
import subprocess

app = FastAPI()

def secure_ping(host: str):
    if not host.isalnum() or '..' in host:
        raise ValueError('Invalid host parameter')
    args = ['ping', '-c', '1', host]
    subprocess.run(args, check=True)

@app.get('/ping')
def ping(host: str):  # Secure implementation using subprocess.call with shell=False and proper argument passing
    return secure_ping(host)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}