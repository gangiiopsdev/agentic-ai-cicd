from fastapi import FastAPI
import subprocess
from typing import Union

app = FastAPI()

async def ping(host: str) -> dict:
    try:
        # Ensure the host input is a valid hostname or IP address
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            return {'status': 'failed', 'error': 'Invalid host'}
        result = subprocess.run(['ping', '-c 1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

@app.get("/ping")
def ping_host(host: str) -> dict:
    return await ping(host)