from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': e.stderr}

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': e.stderr}