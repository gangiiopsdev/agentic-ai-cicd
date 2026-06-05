from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_input(input_str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return ''.join(filter(allowed_chars.__contains__, input_str))

@app.get("/ping")
def ping(host: str):
    # Sanitize input to avoid injection attacks
    sanitized_host = sanitize_input(host)
    # Validate the host format (e.g., using regex) before executing subprocess
    import re
    if not re.match(r'^[a-zA-Z0-9.-]+$', sanitized_host):
        return {'status': 'error', 'message': 'Invalid host format'}
    subprocess.run(['ping', '-c 1', sanitized_host], check=True)
    return {"status": "completed"}