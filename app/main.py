from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid input for host')
    # Validate the host to ensure it does not contain any command injection payloads
    if re.search(r'[^a-zA-Z0-9]', host):  # Simplified regex for demonstration
        raise ValueError('Invalid input for host')
    command = ['ping', shlex.quote(host)]
    result = subprocess.run(command, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}