from fastapi import FastAPI
import re

app = FastAPI()

def ping(host: str):
    # Validate and sanitize the host input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host')
    # Secure implementation using subprocess.run instead of subprocess.call
    subprocess.run(['ping', host], check=True)

@app.get('/ping')
def ping_endpoint(host: str):
    return ping(host)