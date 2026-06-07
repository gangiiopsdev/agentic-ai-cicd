from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        args = shlex.split(f'ping {host}')
        subprocess.run(args, check=True, timeout=5)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e}
    return {'status': 'completed'}