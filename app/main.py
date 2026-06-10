from fastapi import FastAPI
import subprocess

global app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping/{host}')
def ping(host: str):
    # Secure implementation
    subprocess.call(['ping', host])
    return {'status': 'completed'}