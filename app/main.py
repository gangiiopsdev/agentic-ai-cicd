from fastapi import FastAPI
import subprocess
import shlex
c import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    args = shlex.split(f'ping {host}')
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout, 'error': result.stderr}

# Fixed code to validate user input
@app.get('/ping_secure')
def ping_secure(host: str):
    if not all(char.isalnum() or char in ('.', '-') for char in host):  # Basic validation
        return {'status': 'error', 'message': 'Invalid input'}
    args = shlex.split(f'ping {host}')
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout, 'error': result.stderr}