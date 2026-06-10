from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Safe implementation to prevent command injection
    subprocess.call(['ping', host])
    return {'status': 'completed'}

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation to prevent command injection
    subprocess.call(['ping', host])
    return {'status': 'completed'}