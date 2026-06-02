from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation with proper validation and escaping
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return f'Ping failed: {e.stderr}'

@app.get("/ping")
def ping_endpoint(host: str):
    # Validate input to prevent injection attacks
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    return ping(host)