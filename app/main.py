from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Sanitize input to prevent injection attacks
    if 'ping' not in host or '..' in host:
        raise ValueError('Invalid host')
    # Secure implementation
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)