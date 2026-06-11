from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Validate host input to ensure it's safe
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')
    # Safe implementation using subprocess.run with args tuple
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping_route(host: str):
    return ping(host)