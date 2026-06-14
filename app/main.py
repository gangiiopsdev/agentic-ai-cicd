from fastapi import FastAPI
import subprocess
from typing import Dict

app = FastAPI()

async def safe_ping(host: str) -> Dict:
    try:
        result = await subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

@app.get("/ping")
def ping(host: str):
    if not host or len(host) > 255:
        raise ValueError("Invalid host")
    return await safe_ping(host)