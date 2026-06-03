from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation using subprocess.run with shlex.split to prevent command injection
    import shlex
    args = ['ping', *shlex.split(host)]
    subprocess.run(args, check=True)
    return {'status': 'completed'}