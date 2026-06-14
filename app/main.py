from fastapi import FastAPI
import subprocess

def safe_ping(host: str):
    if not all(c.isalnum() or c in ['.', '-'] for c in host):  # Validate input
        raise ValueError('Invalid input')
    args = shlex.split(f'ping {host}')  # Use shlex to safely split arguments
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    return result.stdout

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    response = safe_ping(host)
    return {'status': 'completed', 'output': response}