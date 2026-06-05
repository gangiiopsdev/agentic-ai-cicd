from fastapi import FastAPI
import asyncio
import ipaddress

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
    allowed_hosts = ['127.0.0.1', 'localhost']  # Only allow specific IPs and localhost for simplicity
    if host in allowed_hosts:
        return True
    return False