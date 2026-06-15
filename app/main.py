from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the host input to prevent injection
    if not validate_host(host):
        raise ValueError('Invalid host name')
    safe_host = shlex.quote(host)
    subprocess.run(['ping', safe_host], capture_output=True, text=True)
    return {'status': 'completed'}

def validate_host(host: str) -> bool:
    # Basic validation: allow only alphanumeric characters and a limited set of symbols
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_.'
    for char in host:
        if char not in allowed_chars:
            return False
    return True