from fastapi import FastAPI
import subprocess
def validate_host(host: str) -> bool:
    allowed_hosts = ['google.com', 'example.com']  # Example whitelist
    return host in allowed_hosts

app = FastAPI()

async def ping(host: str):
    if not validate_host(host):
        raise ValueError('Invalid hostname')
    args = ['ping', host]
    subprocess.run(args, check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    return await ping(host)