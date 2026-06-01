from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation with validation
    if host.startswith('192.168.') or host.startswith('10.'):
        subprocess.run(['ping', host], check=True)
    else:
        raise ValueError('Invalid host for pinging')

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)