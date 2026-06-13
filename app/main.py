from fastapi import FastAPI
import subprocess
from typing import Optional

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate host input
    allowed_hosts = ['example.com', 'localhost']
    if host not in allowed_hosts:
        return {'status': 'error', 'message': 'Invalid host'}
    args = ['ping', '-c', '1', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}