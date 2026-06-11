from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate the input to ensure it does not contain malicious content
    if 'ping' in host or ';' in host or '&' in host:
        raise ValueError('Invalid input detected')
    # Secure implementation using subprocess.run()
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}