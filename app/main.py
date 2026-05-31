from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate host to prevent command injection
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}