from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate the input to ensure it does not contain malicious commands
    if not host.isalnum() and '_' not in host:
        return {'error': 'Invalid input'}, 400
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True)

    return {'status': 'completed'}