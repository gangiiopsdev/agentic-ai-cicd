from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    cmd = ['ping'] + [arg for arg in shlex.split(host) if arg.isalnum()]
    subprocess.call(cmd)
    return {'status': 'completed'}