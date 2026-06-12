from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def safe_ping(host: str):
    if not host or host.strip() == 'localhost':
        raise ValueError('Invalid host')
    # Validate and sanitize input
    sanitized_host = re.sub(r'[^a-zA-Z0-9.-]', '', host)
    try:
        result = subprocess.run(['/bin/ping', '-c', '1', sanitized_host], capture_output=True, text=True, check=True)
        return {'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

@app.get('/ping')
def ping(host: str):
    return await safe_ping(host)