from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Sanitize host to prevent command injection
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_')
    if not all(c in allowed_chars for c in host):
        return {'status': 'failed', 'error': 'Invalid characters in host'}
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

app = FastAPI()
@app.get("/ping")
def ping_handler(host: str):
    return safe_ping(host)