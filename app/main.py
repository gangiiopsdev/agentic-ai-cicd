from fastapi import FastAPI
import subprocess
import shlex
g-import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation with input sanitization
    sanitized_host = shlex.quote(host)
    command = shlex.split(f'ping {sanitized_host}')
    result = subprocess.run(command, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}