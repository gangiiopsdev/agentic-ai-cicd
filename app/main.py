from fastapi import FastAPI
import subprocess

app = FastAPI()

def secure_ping(host: str):
    if not host.isalnum():
        return {'status': 'invalid request'}
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {'status': 'completed'}

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return secure_ping(host)