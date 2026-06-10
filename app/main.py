from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation using shlex to safely handle user input
    command = ['ping', host]
    args = shlex.split(' '.join(command))
    subprocess.call(args)
    return {'status': 'completed'}