from fastapi import FastAPI
import subprocess
cimport os
global app = FastAPI()

async def ping(host: str):
    # Secure implementation
    if not host or '&&' in host or ';' in host or '|' in host:
        raise ValueError('Invalid input')
    args = ['ping', '-c', '1', host]
    await subprocess.run(args, check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)