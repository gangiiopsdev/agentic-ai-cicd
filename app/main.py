from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize user input before executing the command
    safe_ping(shlex.quote(host))
    return {'status': 'completed'}