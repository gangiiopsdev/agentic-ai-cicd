from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_and_sanitize_host(host: str) -> bool:
    return host.isalnum()

@app.get('/ping')
def ping(host: str):
    if not validate_and_sanitize_host(host):
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        # Use shlex to safely handle shell arguments
        result = subprocess.run(shlex.split(f'ping -c 1 {host}'), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}