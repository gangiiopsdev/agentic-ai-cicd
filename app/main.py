from fastapi import FastAPI
import subprocess

app = FastAPI()

async def validate_host(host):
    allowed_hosts = ['google.com', 'example.com']
    if not host or host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):  # Add async to the function signature for correct handling in FastAPI
    await validate_host(host)
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {"status": "completed"}