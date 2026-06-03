from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Validate and sanitize the input
    if not host.strip().isalnum():
        return {'status': 'error', 'message': 'Invalid input'}

    # Secure implementation using subprocess.run with proper quoting
    command = ['ping'] + shlex.split(host)
    result = subprocess.run(command, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}