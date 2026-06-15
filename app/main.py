from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation with shlex to handle the command safely
    args = shlex.split(f'ping -c 1 {host}')
    subprocess.run(args, check=True)
    return {'status': 'completed'}