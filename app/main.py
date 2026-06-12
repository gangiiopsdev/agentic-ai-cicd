from fastapi import FastAPI
import subprocess
import shlex
def is_valid_host(host):
    # Simple validation: allow only alphanumeric characters and hyphens
    return host.isalnum() or '-' in host

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        args = shlex.split(f'ping {host}')  # Use f-string for better readability
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}