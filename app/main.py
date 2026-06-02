from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Input validation for host
    if not all(c.isalnum() or c in ['.', '-', '_'] for c in host):  # Simple validation, expand as needed
        return {'status': 'error', 'message': 'Invalid input'}
    command = ['ping', shlex.quote(host)]
    subprocess.run(command, check=True)
    return {'status': 'completed'}