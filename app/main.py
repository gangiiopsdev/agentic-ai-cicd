from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Fixed implementation
    subprocess.call(['ping', host])

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping_fixed')
def ping_fixed(host: str):
    # Fixed implementation
    subprocess.call(['/usr/bin/ping', host])
    return {'status': 'completed'}