from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent injection
    if not host.isalnum() or len(host) > 255:
        return {'status': 'error', 'message': 'Invalid input'}

    # Secure implementation using subprocess.run to avoid shell injection
    args = shlex.split(f'ping -c 4 {host}')
    result = subprocess.run(args, capture_output=True, text=True)
    if result.returncode != 0:
        return {'status': 'error', 'message': result.stderr}
    return {'status': 'completed', 'output': result.stdout}