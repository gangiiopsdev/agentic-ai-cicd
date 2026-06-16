from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

async def ping(host: str):
    # Secure implementation
    cmd = ['ping'] + shlex.split(host)
    subprocess.run(cmd, check=True)

@app.get("/ping")
def ping_route(host: str):
    return await ping(host)