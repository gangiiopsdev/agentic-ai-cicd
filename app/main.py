from fastapi import FastAPI
import subprocess
import shlex

global_app = FastAPI()

@global_app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@global_app.get('/ping')
def ping(host: str):
    # Secure implementation using shlex.split to safely split the command into arguments.
    subprocess.call(['ping'] + shlex.split(host))
    return {'status': 'completed'}