from fastapi import FastAPI
import subprocess
import shlex

def safe_ping(host: str):
    # Validate and sanitize host input
    if not host.isalnum():
        raise ValueError('Invalid host name')
    args = ['ping', shlex.quote(host)]
    subprocess.run(args, shell=False)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}