from fastapi import FastAPI
import subprocess
import re
import asyncio

app = FastAPI()

async def safe_ping(host: str):
    # Validate the host using a more robust method
    if not is_safe_host(host):
        raise Exception('Host is not allowed')

    # Using subprocess.run instead of subprocess.call and avoiding shell=True
    result = await asyncio.to_thread(subprocess.run, ['ping', '-c', '1', host], capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        raise Exception('Host is not allowed')
    return safe_ping(host)

def is_safe_host(host: str):
    # Implement a more robust list of allowed hosts or patterns
    allowed_hosts = ['127.0.0.1', 'localhost', '192.168.1.*']  # Add more patterns as needed
    for pattern in allowed_hosts:
        if re.match(pattern, host):
            return True
    return False