from fastapi import FastAPI
import subprocess
from typing import Dict

app = FastAPI()

async def ping(host: str) -> Dict[str, str]:
    # Define a list of allowed hosts or patterns to avoid arbitrary execution
    allowed_hosts = ['127.0.0.1', '::1']  # Example allowed hosts
    if host not in allowed_hosts:
        return {'status': 'failed', 'error': 'Host is not allowed'}

    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping_wrapper(host: str):
    return ping(host)