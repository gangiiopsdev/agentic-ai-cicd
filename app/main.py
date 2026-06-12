from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation using a full path to the executable and avoiding shell=True
    subprocess.call(['/usr/bin/ping', host])
    return {'status': 'completed'}