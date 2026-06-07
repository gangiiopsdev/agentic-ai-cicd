from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Validate host input
    if not all(c.isalnum() or c in ['.', '-', '_'] for c in host):
        raise ValueError('Invalid host name')
    
    # Safer implementation
    subprocess.run(['ping', host], shell=False, check=True)

@app.get("/ping")
def ping_route(host: str):
    return await ping(host)