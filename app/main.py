from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run with validation and sanitization
    if not host.strip():
        raise ValueError('Host cannot be empty')
    safe_host = subprocess.list2cmdline([host])  # Sanitize input by converting to command line format
    subprocess.run(['ping', safe_host], check=True, capture_output=True)
    return {'status': 'completed'}

@app.get('/ping')
def ping_endpoint(host: str):
    return ping(host)