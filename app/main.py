from fastapi import FastAPI
import subprocess
import shlex
global_params = dict(encoding='utf-8', text=True)

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation using subprocess.run for better control and security
    command = shlex.split(f'ping {host}')
    result = subprocess.run(command, **global_params, capture_output=True)
    return {'status': 'completed', 'output': result.stdout}