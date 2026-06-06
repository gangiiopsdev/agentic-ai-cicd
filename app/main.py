from fastapi import FastAPI
import subprocess
from typing import Optional

app = FastAPI()

allowed_hosts = ['127.0.0.1', '::1']

@app.get("/ping")
def ping(host: str) -> dict:
    if host not in allowed_hosts:
        return {'error': 'Invalid host'}

    command = ['ping', '-c', '1', host]  # Use -c option to limit the number of pings
    subprocess.run(command, check=True)
    return {"status": "completed"}