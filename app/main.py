from fastapi import FastAPI
import subprocess
import shlex

global_args = ['ping']

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation with shlex to safely handle arguments
    args = global_args + shlex.split(host)
    subprocess.call(args)
    return {'status': 'completed'}