from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

async def safe_ping(host: str):
    # Validate host input to only allow valid IP addresses or domain names
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host format')
    try:
        output = await asyncio.to_thread(subprocess.check_output, ['ping', host], universal_newlines=True, timeout=5)
        return output
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    result = await safe_ping(host)
    return {'status': 'completed', 'result': result}