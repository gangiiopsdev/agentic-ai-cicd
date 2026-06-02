from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Safer implementation using subprocess.run to avoid shell=True and partial paths
    result = await asyncio.to_thread(subprocess.run, ['ping', host], capture_output=True, text=True, check=True)
    return result.stdout

@app.get("/ping")
def ping_endpoint(host: str):
    if not is_valid_host(host):
        raise ValueError('Invalid host')
    return await ping(host)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

def is_valid_host(host: str) -> bool:
    # Implement validation logic here, e.g., check if the host is a known good IP or domain
    return True