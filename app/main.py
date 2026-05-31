from fastapi import FastAPI
import subprocess
from typing import List

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        return {'status': 'error', 'message': 'Invalid host'}
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}