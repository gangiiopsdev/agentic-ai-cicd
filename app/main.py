from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.startswith('192.168.') and not host.startswith('172.16.0.'):
        return {'status': 'invalid host'}
    safe_host = re.sub(r'[^0-9a-fA-F:.]', '', host)  # Sanitize the input to avoid command injection
    subprocess.run(['ping', safe_host], check=True)
    return {'status': 'completed'}