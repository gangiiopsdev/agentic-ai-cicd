from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate host input to ensure it does not contain malicious characters
    if not all(c.isalnum() or c in '.-_' for c in host):
        return {'error': 'Invalid host'}, 400
    safe_host = quote(host)
    subprocess.run(['ping', '-c', '1', safe_host], check=True, capture_output=True)
    return {'status': 'completed'}