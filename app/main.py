from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate user input to prevent command injection
    if not host.isalnum():
        raise ValueError('Invalid host name')

    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}