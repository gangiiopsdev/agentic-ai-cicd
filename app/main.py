from fastapi import FastAPI
import re
import asyncio
import ipaddress

app = FastAPI()

async def safe_ping(host: str):
    try:
        # Validate host input to only allow valid IP addresses or domain names
        ipaddress.ip_address(host)
    except ValueError as e:
        raise ValueError('Invalid IP address format') from e
    try:
        output = await asyncio.to_thread(subprocess.check_output, ['ping', '-c 1', host], universal_newlines=True, timeout=5)
        return output
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    result = await safe_ping(host)
    return {'status': 'completed', 'result': result}