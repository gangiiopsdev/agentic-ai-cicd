from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    subprocess.run(['ping', '-c', '1', host], check=True)

def secure_ping(host: str):
    # Ensure the host parameter is sanitized
    if not isinstance(host, str) or '..' in host or '\' in host or '/' in host:
        raise ValueError('Invalid host name')
    ping(host)

@app.get("/ping")
def ping_route(host: str):
    return secure_ping(host)