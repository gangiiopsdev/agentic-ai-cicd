from fastapi import FastAPI
import subprocess
def sanitize_input(input_str):
    # Simple sanitization, in production use a proper library or function
    return ''.join(e for e in input_str if e.isalnum() and 'a' <= e <= 'z')

def safe_ping(sanitized_host):
    try:
        result = subprocess.run(['ping', sanitized_host], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not is_safe_hostname(sanitized_host):
        raise ValueError("Invalid hostname")
    return safe_ping(sanitized_host)

def is_safe_hostname(hostname):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-')
    for char in hostname:
        if char not in allowed_chars or (char == '-' and (hostname.startswith('-') or hostname.endswith('-'))):
            return False
    return True