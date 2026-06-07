from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize input using shlex
    safe_host = shlex.quote(host)
    args = ['ping', safe_host]
    subprocess.run(args, check=True)
    return {'status': 'completed'}