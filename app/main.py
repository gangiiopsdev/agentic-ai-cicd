from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    if not host.isalnum():
        raise ValueError('Invalid hostname')

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    validate_host(host)
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {'status': 'completed'}