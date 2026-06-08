from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Validate host input
    if not validate_host(host):
        return None

    # Secure implementation using subprocess.run
    result = await asyncio.to_thread(subprocess.run, ['ping', host], capture_output=True, text=True)
    return result.stdout

async def validate_host(host: str) -> bool:
    allowed_hosts = ['example.com', 'test.com']  # List of allowed hosts
    return host in allowed_hosts

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)