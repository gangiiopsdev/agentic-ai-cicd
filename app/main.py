from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate input to prevent command injection
    if not host or ' ' in host:
        return {'status': 'error', 'message': 'Invalid input'}
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}