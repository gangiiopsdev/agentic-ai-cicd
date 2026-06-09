from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate host input
    if not all(c.isalnum() or c in ['.', '-', '_'] for c in host) or len(host.split('.')) != 4:
        raise ValueError('Invalid host name')
    
    # Safer implementation
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping_route(host: str):
    return {'result': 'Pinging', 'host': host}