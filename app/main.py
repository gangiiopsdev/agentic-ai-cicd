from fastapi import FastAPI
import subprocess
from typing import List

app = FastAPI()

def ping(host: str):
    if not host.strip():
        raise ValueError('Invalid host provided')
    args = ['ping', '-c', '1', f'{host}']
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    return {'status': 'completed' if result.returncode == 0 else 'failed', 'output': result.stdout}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)