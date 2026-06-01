from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run with proper validation
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid hostname')
    result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}