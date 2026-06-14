from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Basic validation to ensure host is safe (e.g., alphanumeric and possibly allowing a limited set of characters)
    if not all(c.isalnum() or c in ['-', '.', '_'] for c in host) or len(host) > 64:
        return False
    return True

def sanitize_host(host):
    # Sanitize input to prevent command injection
    sanitized_host = ''.join(e for e in host if e.isalnum() or e in ['-','.', '_', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'])
    return sanitized_host

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if validate_host(sanitized_host):
        subprocess.call(['ping', sanitized_host], shell=False)
        return {"status": "completed"}
    else:
        return {"error": "Invalid host"}