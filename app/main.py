from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Validate the host input to ensure it contains only allowed characters
    if not all(c.isalnum() or c in '-.' for c in host):
        raise ValueError('Invalid host input')
    args = ['ping', shlex.quote(host)]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}