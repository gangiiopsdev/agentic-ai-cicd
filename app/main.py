from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    try:
        args = shlex.split(f'ping {shlex.quote(host)}')
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if host in ['localhost', '127.0.0.1']:  # Limit access to local hosts
        return safe_ping(host)
    else:
        return {'status': 'failed', 'error': 'Invalid host'}