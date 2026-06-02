from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation using shlex for safe command execution
    cmd = ['ping', shlex.quote(host)]
    subprocess.call(cmd)
    return {'status': 'completed'}