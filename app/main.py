from fastapi import FastAPI
import re
import asyncio
import subprocess

app = FastAPI()

def safe_ping(host: str) -> str:
    # Validate host input to only allow valid IP addresses or domain names
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host format')
    try:
        output = subprocess.check_output(['ping', '-c 1', re.escape(host)], universal_newlines=True, timeout=5)
        return output
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    return {'status': 'completed', 'result': result}