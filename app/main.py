from fastapi import FastAPI
import subprocess
from shlex import quote
import os

app = FastAPI()

def safe_ping(host: str):
    try:
        # Validate host input before using it in the command
        if not host or 'localhost' in host or '127.0.0.1' in host or '::1' in host or '0.0.0.0' in host or ':' in host.split(':')[0]:
            raise ValueError('Invalid host')
        command = ['ping', quote(host)]
        response = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        return response.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {"status": "completed", "result": result}