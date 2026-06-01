from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Sanitize host to prevent injection attacks
    if '@' in host or '/' in host or ' ' in host:
        raise ValueError('Invalid hostname')
    args = shlex.split(f'ping {host}')
    result = subprocess.run(args, capture_output=True, text=True, timeout=5)
    return {'status': 'completed', 'output': result.stdout}

@app.get('/ping')
def ping(host: str):
    try:
        return safe_ping(host)
    except ValueError as e:
        return {'status': 'failed', 'error': str(e)}