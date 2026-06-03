from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def execute_ping(host: str):
    # Sanitize input to prevent shell injection
    safe_host = ''.join(c for c in host if c.isalnum() or c in (".-",))
    cmd = shlex.split(f'ping {safe_host}')
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    output = execute_ping(host)
    return {'status': 'completed', 'output': output}