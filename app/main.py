from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation with absolute path and shell=False
    subprocess.run(['/usr/bin/ping', host], check=True, shell=False)
    return {'status': 'completed'}