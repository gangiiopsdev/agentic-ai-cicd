from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the input to prevent command injection
    if not all(c.isalnum() or c in '-.' for c in host):
        raise ValueError('Invalid characters in host name')
    result = subprocess.run(['ping', *shlex.split(f'"{host}"')], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}