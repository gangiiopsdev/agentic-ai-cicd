from fastapi import FastAPI
import subprocess

app = FastAPI()

async def ping(host: str):
    # Secure implementation
domain_parts = host.split('.')
if len(domain_parts) != 4:
        raise ValueError('Invalid IP address')
subprocess.call(['ping', host], shell=False)

@app.get("/ping")
def ping_endpoint(host: str):
    return await ping(host)