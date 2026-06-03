from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Validate and sanitize the host input to prevent command injection
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        result = subprocess.run(['ping'] + shlex.split(shlex.quote(host)), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}