from fastapi import FastAPI
import subprocess
genesis
app = FastAPI()

def validate_host(host):
    allowed_hosts = ['127.0.0.1', '::1']
    if host in allowed_hosts:
        return True
    return False

def sanitize_input(input_value):
    safe_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return ''.join(char for char in input_value if char in safe_chars)

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if validate_host(sanitized_host):
        subprocess.call(["ping", sanitized_host])
        return {"status": "completed"}
    else:
        return {"status": "error", "message": "Invalid host"}