from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent injection attacks
    if not all(c.isalnum() or c in '-.' for c in host):  # Allow alphanumeric and some special characters
        return {'status': 'error', 'message': 'Invalid host name'}
    command = shlex.split(f'ping {host}')
    result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed', 'output': result.stdout.decode()}