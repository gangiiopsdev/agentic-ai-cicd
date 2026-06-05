from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using shlex.split
    args = shlex.split(f'ping {host}')
    subprocess.call(args)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Using a safe function to avoid injection
    safe_ping(host)
    return {'status': 'completed'}