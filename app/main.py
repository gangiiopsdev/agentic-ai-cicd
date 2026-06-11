from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent injection
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid input'}
    
    # Secure implementation using subprocess.run to avoid shell injection
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True)
    return {'status': 'completed'}