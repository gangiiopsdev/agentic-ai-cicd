from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Safe implementation
    args = ['ping', shlex.quote(host)]
    subprocess.call(args)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_safe(host: str):
    # Safe implementation
    args = ['ping', shlex.quote(host)]
    subprocess.call(args)
    return {'status': 'completed'}