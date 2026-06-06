from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate the host to ensure it does not contain malicious content
    if not host.isalnum() or '.' not in host:
        raise ValueError('Invalid host name')
    # Secure implementation using subprocess.run
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping_route(host: str):    
    return ping(host)