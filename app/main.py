from fastapi import FastAPI
import subprocess
import shlex
from typing import List

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate host input (e.g., allowed IP ranges)
    try:
        ip_parts = host.split('.')
        if len(ip_parts) != 4 or any(not part.isdigit() for part in ip_parts) or any(int(part) > 255 for part in ip_parts):
            raise ValueError('Invalid host input')
    except Exception as e:
        return {'status': str(e)}

    command = shlex.split(f'ping {host}')
    result = subprocess.run(command, capture_output=True, text=True, check=False)
    return {'status': result.stdout}