from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Secure implementation
    if host.strip() == 'localhost' or host.startswith('127.0.0.1'):
        subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping_route(host: str):
    return await ping(host)