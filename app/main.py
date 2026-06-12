from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate input
    if not host or ' ' in host:
        return {'status': 'failed', 'error': 'Invalid host'}

    # Secure implementation using subprocess.run with proper validation and sanitization
    try:
        host = shlex.quote(host)
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}