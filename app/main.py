from fastapi import FastAPI
import subprocess
import os

app = FastAPI()

def ping(host: str):
    # Secure implementation
    if host.strip().startswith('-'):  # Check for potential malicious flags
        raise ValueError('Invalid input detected')
    subprocess.run(['ping', '-c', '4', os.path.expanduser(host)], check=True)

@app.get("/ping")
def ping_route(host: str):
    return ping(host)