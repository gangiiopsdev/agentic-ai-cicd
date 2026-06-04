from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the host input to ensure it does not contain malicious characters
    if not host.isalnum() or '.' in host:
        return {'status': 'error', 'message': 'Invalid host input'}
    # Use shlex.split to safely handle user inputs
    args = shlex.split(f'ping {host}')
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}