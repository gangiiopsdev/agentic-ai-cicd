from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Secure implementation with input validation and sanitization
    if not host.isalnum():
        raise ValueError('Invalid input')
    command = ['ping', shlex.quote(host)]
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}