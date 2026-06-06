from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()

async def ping(host: str):
    # Validate host input
    if not all(char.isalnum() or char in '-.' for char in host):
        raise ValueError('Invalid host name')
    args = ['ping', *shlex.split(host)]
    subprocess.run(args, check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    return {'result': 'Pinging host', 'host': host}