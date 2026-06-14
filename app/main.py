from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(filter(lambda x: x in allowed_chars, host))

def is_valid_host(host):
    import re
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {"status": "invalid_host", "message": "Host contains disallowed characters."}, 400
    sanitized_host = sanitize_host(host)
    # Safe implementation using subprocess.run instead of subprocess.call
    result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}