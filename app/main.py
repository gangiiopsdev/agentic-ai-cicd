from fastapi import FastAPI
import subprocess

async def ping(host: str):
    # Validate and sanitize the host parameter to prevent injection attacks
    if not is_valid_host(host):
        raise ValueError("Invalid hostname")
    args = ['ping', host]
    subprocess.run(args, check=True)

def is_valid_host(hostname: str) -> bool:
    # Implement validation logic here
    return hostname.isalnum() and '.' in hostname