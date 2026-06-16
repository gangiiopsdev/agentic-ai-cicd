from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate host input
    if not all(c.isalnum() or c in ['.', '-', '_'] for c in host):
        raise ValueError('Invalid host name')
    # Secure implementation using subprocess.run with list argument
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping_route(host: str):
    return {'host': host, 'status': 'Pinging...'}