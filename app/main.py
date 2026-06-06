from fastapi import FastAPI
import asyncio
import ipaddress
import re

app = FastAPI()

async def safe_ping(host: str):
    # Validate the host using a more robust method
    if not is_safe_host(host):
        raise Exception('Host is not allowed')

    try:
        ipaddress.ip_address(host)
    except ValueError:
        raise Exception('Invalid IP address format')

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
    allowed_hosts_pattern = r'^\b(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b$'  # Regex to validate IP address
    if re.match(allowed_hosts_pattern, host):
        return True
    return False