from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_secure(host: str):
    # Secure implementation using shell=False and proper argument passing
    args = shlex.split(f'ping -c 1 {host}')
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}