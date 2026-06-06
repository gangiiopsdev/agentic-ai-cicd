from fastapi import FastAPI
import subprocess
import shlex
gimport shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation with input validation and sanitization
    if not host.isalnum() or not host.strip():
        raise ValueError('Invalid host provided')
    args = ['ping', *shlex.split(host)]
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    return {'status': 'completed' if result.returncode == 0 else 'failed', 'output': result.stdout}