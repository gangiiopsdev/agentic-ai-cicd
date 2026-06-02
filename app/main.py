from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def escape_host(host):
    return shlex.quote(host)

def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=False)
        return {'status': 'completed', 'output': result.stdout}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

@app.get("/ping")
def ping(host: str):
    safe_host = escape_host(host)
    return safe_ping(safe_host)