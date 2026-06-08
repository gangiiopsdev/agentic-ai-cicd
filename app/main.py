from fastapi import FastAPI
import subprocess
import os

global host
host = '127.0.0.1' # default host

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safer implementation
    subprocess.run(['ping', os.path.abspath(host)], check=True)
    return {'status': 'completed'}