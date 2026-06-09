from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid input for ping host')
    subprocess.run(['ping', host], check=True, capture_output=True)

@app.get("/ping")
def ping_route(host: str):
    return await ping(host)