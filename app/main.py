from fastapi import FastAPI
import subprocess
from typing import Dict

app = FastAPI()

def safe_ping(host: str) -> Dict[str, str]:
    if host not in ['example.com', 'localhost']:  # Add a whitelist of allowed hosts
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

@app.get("/ping")
def ping(host: str) -> Dict[str, str]:
    return safe_ping(host)