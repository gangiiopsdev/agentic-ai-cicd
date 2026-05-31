from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate the host input to prevent command injection
    if not host.isalnum() and not '.' in host:
        return {'status': 'error', 'message': 'Invalid hostname'}
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}