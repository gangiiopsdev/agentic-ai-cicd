from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Validate the host input to ensure it does not contain malicious content
    if not host.isdigit() or len(host) != 3:
        return {'status': 'error', 'message': 'Invalid host input'}
    args = shlex.split(f'ping {host}')  # Use f-string for safer construction
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}