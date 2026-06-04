from fastapi import FastAPI
import subprocess
cimport shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation
    safe_host = shlex.quote(host)
    args = shlex.split(f'ping {safe_host}')
    subprocess.run(args, check=True)
    return {'status': 'completed'}