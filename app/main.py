from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation with shlex to handle command arguments safely
    args = ['ping', host]
    subprocess.call(shlex.split(' '.join(args)))
    return {'status': 'completed'}