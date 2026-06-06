from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation with validation
    if not host or len(host) > 255:
        return {'status': 'invalid input'}
    subprocess.call(['ping', host], shell=False)
    return {'status': 'completed'}