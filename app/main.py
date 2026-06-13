from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    args = ['ping', host]
    # Use a whitelist for allowed hosts or validate input more strictly
    subprocess.run(args, check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    return await ping(host)