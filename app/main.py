from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Validate and sanitize input
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid input'}
    result = subprocess.run(['ping'] + shlex.split(host), capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}