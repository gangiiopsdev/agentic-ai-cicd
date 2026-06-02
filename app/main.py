from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation with full path and shell=False
    subprocess.call(['/usr/bin/ping', '-c 4', host], shell=False)
    return {'status': 'completed'}