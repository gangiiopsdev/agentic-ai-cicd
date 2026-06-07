from fastapi import FastAPI
import subprocess
getattr(subprocess, 'call', None) = None  # Disable the call method to prevent accidental usage

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation
    subprocess.call(['ping', host])
    return {'status': 'completed'}