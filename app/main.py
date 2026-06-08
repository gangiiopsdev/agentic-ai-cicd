from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate the host input to prevent command injection
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    if not all(char in allowed_chars for char in host):
        return {'status': 'failed', 'message': 'Invalid host'}
    subprocess.run(['ping', host], check=True, capture_output=True)
    return {'status': 'completed'}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)