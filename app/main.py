from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the host input
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid input'}

    # Secure implementation using subprocess.run with shlex.split for safe argument splitting
    result = subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True, shell=False)
    return {'status': 'completed', 'output': result.stdout}