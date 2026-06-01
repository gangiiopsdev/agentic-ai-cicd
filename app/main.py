from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using subprocess.run
    subprocess.run(['ping', host], check=True, timeout=5)

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent command injection
    if not all(c.isalnum() or c in ('-', '.', '_') for c in host):
        return {'error': 'Invalid host'}, 400
    safe_ping(host)
    return {'status': 'completed'}