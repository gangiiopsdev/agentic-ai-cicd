from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        # Use subprocess.run instead of subprocess.call and avoid shell=True
        subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    # Validate host to prevent command injection attacks
    if not is_valid_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    return safe_ping(host)

def is_valid_host(host: str) -> bool:
    # Implement validation logic for the host parameter
    import re
    pattern = re.compile(r'^[a-zA-Z0-9.-]+$')
    return bool(pattern.match(host))