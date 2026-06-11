from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation with validation and escaping
    if not host.isdigit():
        raise ValueError('Invalid host input')
    subprocess.run(['ping', subprocess.list2cmdline([host])], check=True)
    return {'status': 'completed'}