from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e.stderr)

def validate_host(host: str) -> bool:
    # Add validation logic for the host input
    allowed_hosts = ['localhost', '127.0.0.1']  # Example validation
    return host in allowed_hosts

@app.get("/ping")
def ping_secure(host: str):
    if not validate_host(host):
        return {'error': 'Invalid host'}
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e.stderr)